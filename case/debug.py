import requests
class Login():
    def __init__(self,s,host):
        self.s = s
        self.host = host
        self.url = host+'/ecmps/login'

    def login(self,phoneNumber,password,proxies=None):
        data = {
            'phoneNumber': phoneNumber,
            'password': password
        }

        url = self.host+'/ecmps/login'
        r = self.s.post(url=url, json=data, verify=False, proxies=proxies).json()
        return r

    def getLoginToken(self,phoneNumber='15527060286',password='hbc23687',proxies=None):
        r = self.login(phoneNumber,password,proxies)
        token = r['data']['token']
        appId = r['data']['apps'][0]['appId']
        return token,appId

class GetUserToken():
    def __init__(self,s,host):
        self.s = s
        self.host = host
        self.url = host+'/ecmps/getUserToken'

    # 获取真正的token接口
    def getUserToken(self,appId,proxies=None):
        params = {
            'appId':appId
        }
        r = self.s.get(url=self.url,params=params,verify=False,proxies=proxies).json()
        return r

    def returnToken(self,appId,proxies=None):
        r = self.getUserToken(appId=appId,proxies=proxies)
        return r['data']['token']

def loginSession(host,proxies,phoneNumber,password):
    s = requests.session()
    l = Login(s,host)
    token, appId = l.getLoginToken(phoneNumber,password,proxies)
    # 获取真正的token
    headers = {
        'appid':appId,
        'Authorization': token
    }
    s.headers.update(headers)
    getToke = GetUserToken(s,host)
    token = getToke.returnToken(appId=appId,proxies=proxies)
    # 将token更新
    headers = {'Authorization': token}
    s.headers.update(headers)
    return s

if __name__ == '__main__':
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    host = 'https://backstageservices.dreawer.com'
    phoneNumber = '15527060286'
    password = 'hbc23687'
    s = loginSession(host=host,proxies=proxies,phoneNumber=phoneNumber,password=password)

    url = 'https://backstageservices.dreawer.com/bsmc/user/getMenu'
    r = s.get(url=url,verify=False,proxies=proxies).json()
    print(r)