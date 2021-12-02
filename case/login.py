import os
import sys
import requests
import urllib3
import allure_pytest
urllib3.disable_warnings()
sys.path.append('./..')
class Login():
    def __init__(self, s, host):
        self.s = s
        self.host = host
        self.url = host+'/ecmps/login'

    def login(self,phoneNumber,password,proxies=None):
        data = {"phoneNumber":phoneNumber,"password":password}
        r = self.s.post(url=self.url,json=data,verify=False,proxies=proxies).json
        return r


    def getTokenAndAppID(self,phoneNumber='15527060286',password='hbc23687',proxies=None):
        r = self.login(phoneNumber,password,proxies)
        token = r['data']['token']
        appid = r['data']['apps'][0]['appId']
        return token,appid

if __name__ == '__main__':
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    s = requests.session()
    l = Login(s,host)
    phoneNumber='15527060286'
    password = 'hbc23687'
    r=l.login(phoneNumber=phoneNumber,password=password,proxies=proxies)
    # token = re.findall('"token":"(.*?)"}}', r.text)
    # appid = re.findall('\[{"appId":"(.*?)"',r.text)
    token,appid = l.getTokenAndAppID(proxies=proxies)
    # token=token[0]
    print(token,appid)
