
import requests


def login(base_url, username, password):
    session = requests.session()
    login_path = '/passport/login'
    login_data = {
        "logintype": "PASSWORD",
        "msg": "",
        "username": username,
        "password": password,
        "cellphone": "",
        "verifycode": ""
    }

    session.post(url=base_url + login_path, data=login_data)
    print("11")

    res = session.get(url=base_url)

    cookieData = res.request.headers.get('Cookie', '')
    # print(cookieData)

    # if 'security_context' in cookieData and (re.findall('company_id=(.+?); security_context=', cookieData)):
    print(cookieData)
    return cookieData
    # else:
    #     print("no")
    #     return ""




if __name__ == '__main__':
    url = 'https://if2b-alpha.casstime.com'
    login(url, username='if2b_admin', password='casstime88')

