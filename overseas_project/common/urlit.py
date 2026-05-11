# coding=utf-8
import logging
import os
import time

import pandas as pd
import xlrd


# 读取入参文件
def readFile(filename):
    with open(file=filename, mode='r', encoding='utf-8') as fread:
        return fread.read().splitlines()


# 读取excel文件.xlsx
def reasxlsx(filename):
    with pd.read_excel(filename) as fread:
        return fread.read()


def strs(row):
    """
    返回一行数据
    :param row:
    :return:
    """

    # try:
    values = ""
    for i in range(len(row)):
        if i == len(row) - 1:
            # 一行遍历结束，换行作为分隔符
            values = values + str(row[i]) + "\n"
        else:
            # 每列数据使用逗号作为分隔符
            values = values + str(row[i]) + ","
    return values
    #
    # except:
    #     raise


# 将excel文件转为带表头的txt文件
def xlsxTotxt(xlsname, txtname):
    """
    ：excel文件转为txt文件
    :param xlsname: excel 文件名
    :param txtname: txt 文件名
    """
    # try:
    data = xlrd.open_workbook(xlsname)
    sqlfile = open(txtname, "a")
    table = data.sheets()[0]   # 表头
    nrows = table.nrows    # 行数
    print(nrows)
    # 如果要跳过表头则将下一行中0改为1
    for ronum in range(1, nrows):
        row = table.row_values(ronum)
        # 将行数拼接成字符串
        values = strs(row)
        # 将字符串写入新文件
        sqlfile.writelines(values)
    sqlfile.close()
    #
    # except:
    #     pass


def getProjectPath(path=os.getcwd()):
    # 读取overseas_project目录所在的位置
    newpath = os.path.join(os.path.dirname(path), 'overseas_project')
    if os.path.isdir(newpath):
        return newpath
    else:
        return getProjectPath(path=os.path.dirname(path))


def reqSet(self, method, path, timeoutsec=1, rename=None, assertavg=None, remark=None, *args, **kwargs):

    with self.clent.request(method=method,
                            url=path,
                            name=path if not rename else rename,
                            timeout=timeoutsec,
                            catch_response=True, *args, **kwargs) as response:

        paramsValue = remark or args or kwargs
        logging.info("接口返回：{}".format(response.text))
        if isinstance(paramsValue, dict) and str(paramsValue).find('headers') != -1:
            del paramsValue['headers']

        if not assertavg:
            if response.status_code == 200:
                response.success()
            # status_code=201亦为正确状态码，少数使用，目前用户web层服务ocr-node服务中
            elif response.status_code == 201:
                response.success()
            else:
                response.failure(f"状态码:{response.status_code},"
                                 f"入参,{paramsValue}"
                                 f"出参:{response.text}"
                                 f"时间:{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}")

        elif isinstance(assertavg, str):
            if response.status_code == 200 and response.text.find(assertavg) != -1:
                response.success()
            else:
                response.failure(f"状态码:{response.status_code},"
                                 f"入参,{paramsValue}"
                                 f"出参:{response.text}"
                                 f"时间:{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}")

        elif isinstance(assertavg, dict):
            '''{"key":None,"value":None}'''
            if response.status_code == 200 and response.json().get(assertavg['key']) == assertavg['value']:
                response.success()
                logging.info(response.text)
            else:
                response.failure(f"状态码:{response.status_code},"
                                 f"入参,{paramsValue}"
                                 f"出参:{response.text}"
                                 f"时间:{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())}")

        return response



