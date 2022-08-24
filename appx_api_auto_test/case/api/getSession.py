import requests
from case.api.loginApi import PcLogin
from case.api.getUserToken import GetUserToken
def getSession(host,proxies,phoneNumber='15527060286',password='hbc23687'):
    s = requests.session()
    # 登录接口，获取登录接口返回的token
    loginToken = PcLogin(s=s,host=host,proxies=proxies).getLoginToken(phoneNumber=phoneNumber,password=password)
    h = {
        'Authorization':loginToken,
        'appid': '1514e1d61686438f95fa46f19070c126'
    }
    # 更新headers
    s.headers.update(h)
    # GetUserToken接口，获取该接口返回的token
    realToken = GetUserToken(s=s,host=host,proxies=proxies).returnRealToken()
    h = {'Authorization':realToken}
    # 再次更新headers
    s.headers.update(h)
    return s
host = 'https://backstageservices.dreawer.com'
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}
getSession(host,proxies)

