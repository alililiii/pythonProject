import os.path
import random

from overseas_project.common.urlit import *


dataPath = str(os.path.join(getProjectPath(), r'if2b\demand_create\data')).replace('\\', '/')

# datatemp = xlsxTotxt(xlsname=dataPath + '/oe1000.xlsx', txtname='./data/oe1000.txt')     # 代客询价批量导入
# batchImport_data = readFile('./data/oe1000.txt')
demandCreate_data = readFile('./data/demand_createData.txt')    # 代客询价

# def get_body_from_res_random():
#     try:
#         with open(r'./data/oe1000.txt', 'a+', encoding='utf-8') as ftemp:
#             for j in range(500):
#                 i = 1
#                 while i < 100:
#                     data = random.choice(batchImport_data)
#                     ftemp.write(data + ',')
#                     i += 1
#                 else:
#                     data_1 = random.choice(batchImport_data)
#                     ftemp.write(data_1 + '\n')
#
#     except FileNotFoundError:
#         print('无法打开指定文件')
#     except LookupError:
#         print('指定了未知编码')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误')
#
#
#
# if __name__ == '__main__':
#     get_body_from_res_random()


