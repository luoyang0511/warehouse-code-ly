class GetUserToken():
    def __init__(self,s,host,proxies=None):
        self.s = s
        self.host = host
        self.proxies = proxies
        self.path ='/ecmps/getUserToken'
        self.url = self.host+self.path

    def getUserToken(self,appId='1514e1d61686438f95fa46f19070c126'):
        '''
        :param appId: appId
        :return: 字典类型的response
        '''
        data = {'appId':appId}
        res = self.s.get(self.url,params=data,proxies=self.proxies,verify=False)
        return res.json()

    def returnRealToken(self):
        '''
        请求getUserToken，获取token
        :return: 接口返回的token
        '''
        token = self.getUserToken()['data']['token']
        return token

if __name__ == '__main__':
    import sys
    import requests
    import loginApi
    s = requests.session()
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    loginToken= loginApi.PcLogin(host=host,s=s,proxies=proxies).getLoginToken()
    h = {
        'Authorization': loginToken,
        'appid': '1514e1d61686438f95fa46f19070c126'
    }
    s.headers.update(h)
    res = GetUserToken(s=s,host=host,proxies=proxies).getUserToken()
    print(res)
