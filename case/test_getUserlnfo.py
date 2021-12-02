import  os
import  sys
import  requests
import  urllib3
import  pytest
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class GetUserInfo():
    def __init__(self,s,host):
        self.s=s
        self.host=host
        self.url=host+'/bsmc/user/getInfo'

    def gestUserInfo(self,proxies=None):
        r=self.s.get(url=self.url,verify=False,proxies=proxies)
        return r


class TestGetUserInfo():
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    def test_gestUserInfo_suess(self,getSession):
        s=getSession
        info=GetUserInfo(s,self.host)
        r=info.gestUserInfo(proxies=self.proxies).json()
        assert r['code'] =='000000'
        assert r['data']['petName']=='超级管理员'
        assert r['comment']=='Completed successfully'

    def test_getUserInfo_fail_02(self):
        s=requests.session()
        h={

        }

        s.headers.update(h)
        info=GetUserInfo(s,self.host)
        r=info.gestUserInfo(proxies=self.proxies)