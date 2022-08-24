import requests

class PcLogin():
    def __init__(self,host,s,proxies=None):
        self.s = s
        self.host = host
        self.proxies = proxies
        self.url =self.host+'/ecmps/login'

    def login(self,phoneNumber='15527060286',password='hbc23687'):
        '''
        login接口
        :param phoneNumber: 用户名，必填，str
        :param password: 密码，必填，str
        :return: 字典类型的response
        '''
        data = {"phoneNumber":phoneNumber,"password":password}
        res = self.s.post(self.url,json=data,proxies=self.proxies,verify=False)
        return res.json()

    def getLoginToken(self,phoneNumber='15527060286',password='hbc23687'):
        '''
        :param phoneNumber: 用户名，必填，str
        :param password: 密码，必填，str
        :return: 接口返回的token
        '''
        res = self.login(phoneNumber,password)
        token = res['data']['token']
        return token

if __name__ == '__main__':
    s = requests.session()
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    res = PcLogin(host=host,s=s,proxies=proxies).login()
    print(res)

