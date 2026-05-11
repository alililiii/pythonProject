
import logging


from overseas_project.common.login import *
from overseas_project.if2b.demand_create.read_data import *



base_url_web = 'https://if2b-alpha.casstime.com'

timeout_second = 1
timeout_second_web = 5

# 登录

# headers = {
#         'Content-Type': 'application/json;charset=UTF-8',
#         'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 '
#                       'Safari/537.36',
#         'Cookie': 'gr_user_id=b64f9c8d-b97c-4e15-897b-35eb34081053; WSESSIONID=b0303ff7-f119-4860-be93-18155c9d77c3; '
#                   'languageCode=zh_CN; ssoAuthCode=OwyRpJ; company_id=; security_context=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9'
#                   '.eyJpc3MiOiJjYXNzbWFsbC5jb20iLCJzdWIiOiIwMDEiLCJhY2NvdW50SWQiOiI2MTllZjJlOGJkMjIzMTAwMDE0YTAzMjIiLCJjbGllbnR'
#                   'JZCI6ImlmMmIiLCJ1c2VybmFtZSI6IjAwMSIsImFuZCI6ImlmMmItYWxwaGEiLCJqdGkiOiIyeFdEN3J0SDU4QzlsYXQ3WDZ4bGpHZ0luVWM'
#                   'zTGVObiIsImlhdCI6MTcyNDcyNDczOCwiZXhwIjoxNzI0NzYwNzM3fQ.BwZ8w-F3INbTSCxfPM-yUwkxTfRkvg0OoQWpjl3bwN2FPvRZNUt'
#                   '-EBwZHg8itQ688nxq0RhzG62u0r43o19pALaoJizHNp5iu50u_h_i62gnAFSQSrpxWQKCz49WDxczA_gtPtLekrLZrSnJlTpM4hBEWGrbbECnxX5lebnt'
#                   '-f0; security_userid=001; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22001%22%2C%22first_id%22%3A%2219131f7e31aa3a'
#                   '-0c4e6157dc9a3b8-26001e51-1474560-19131f7e31bd5f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B'
#                   '%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC'
#                   '_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219131f7e31aa3a'
#                   '-0c4e6157dc9a3b8-26001e51-1474560-19131f7e31bd5f%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxNDVhMzEwO'
#                   'TUyNTUtMGI0MzE3MWI1MjFhNDQ4LTI2MDAxZTUxLTIwNzM2MDAtMTkxNDVhMzEwOTYxNWJlIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMDAxIn0%3D%22%2C%'
#                   '2history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22001%22%7D%7D'
#     }

cookie = login(base_url_web, username='if2b_admin', password='casstime88')
logging.info(cookie)
print("cookie   " + cookie)

def update_single_headers(user):
    """
    指定用户登录
    :param user:
    :return:
    """
    user.client.headers.update({'Content-Type': 'application/json;charset=UTF-8'})
    # user.client.headers.update({'Cookie': 'gr_user_id=b64f9c8d-b97c-4e15-897b-35eb34081053; WSESSIONID=b0303ff7-f119-4860-be93-18155c9d77c3; languageCode=zh_CN; ssoAuthCode=OwyRpJ; company_id=; security_context=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjYXNzbWFsbC5jb20iLCJzdWIiOiIwMDEiLCJhY2NvdW50SWQiOiI2MTllZjJlOGJkMjIzMTAwMDE0YTAzMjIiLCJjbGllbnRJZCI6ImlmMmIiLCJ1c2VybmFtZSI6IjAwMSIsImFuZCI6ImlmMmItYWxwaGEiLCJqdGkiOiIyeFdEN3J0SDU4QzlsYXQ3WDZ4bGpHZ0luVWMzTGVObiIsImlhdCI6MTcyNDcyNDczOCwiZXhwIjoxNzI0NzYwNzM3fQ.BwZ8w-F3INbTSCxfPM-yUwkxTfRkvg0OoQWpjl3bwN2FPvRZNUt-EBwZHg8itQ688nxq0RhzG62u0r43o19pALaoJizHNp5iu50u_h_i62gnAFSQSrpxWQKCz49WDxczA_gtPtLekrLZrSnJlTpM4hBEWGrbbECnxX5lebnt-f0; security_userid=001; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22001%22%2C%22first_id%22%3A%2219131f7e31aa3a-0c4e6157dc9a3b8-26001e51-1474560-19131f7e31bd5f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219131f7e31aa3a-0c4e6157dc9a3b8-26001e51-1474560-19131f7e31bd5f%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxNDVhMzEwOTUyNTUtMGI0MzE3MWI1MjFhNDQ4LTI2MDAxZTUxLTIwNzM2MDAtMTkxNDVhMzEwOTYxNWJlIiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMDAxIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22001%22%7D%7D'})
    user.client.headers.update({'Cookie': cookie})

    return cookie

def demand_create(user):
    """
    代客询价接口
    :param user:
    :return:
    """
    # web层接口需要先登录获取cookie
    update_single_headers(user)

    data = random.choice(demandCreate_data)
    reqSet(
        self=user,
        method='POST',
        rename='/customer-web/customer/demand/create',
        json=json.loads(data),
        path=f'/customer-web/customer/demand/create',
        timeoutsec=timeout_second
    )





