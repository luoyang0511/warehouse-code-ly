import urllib3
urllib3.disable_warnings()
class GetUserInfo():
    def __init__(self,s,host,proxies=None):
        self.s = s
        self.host = host
        self.proxies = proxies
        self.url =self.host+'/bsmc/user/getInfo'

    def getUserInfo(self):
        res = self.s.get(url=self.url,proxies=self.proxies,verify=False)
        return res.json()


if __name__ == '__main__':
    from case.api.getSession import getSession
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    s=getSession(host,proxies)
    res=GetUserInfo(s=s,host=host,proxies=proxies)
    print(res)