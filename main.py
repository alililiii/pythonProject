# This is a sample Python script.
from overseas_project.common.login import login


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import requests

    host = 'https://if2b-alpha.casstime.com'

    login(host, username='if2b_admin', password='casstime88')

    # url = '/passport/login'
    url = '/supply-web/supply/demands/page?languageCode=zh_CN'

    body = {
      "page": 1,
      "size": 10,
      "demandId": "",
      "statusIds": [
        "UNQUOTE"
      ],
      "organizationIdList": [],
      "commitStartDate": 1716536162807,
      "commitEndDate": 1724515199999
    }

    req = requests.post(url=host+url,data=body)
    print(req.request.path_url)
    print(req.content)

