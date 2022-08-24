import urllib3
urllib3.disable_warnings()
#新增复制优惠券
class GetCounponadd:

    def __init__(self,s,host,proxies=None):
        self.s=s
        self.host=host
        self.proxies=proxies
        self.url=host+'/mc/business/coupon/add'

    def getCounponadd(self,name):
        data ={"applicableScope":"WHOLE","conditionType":"DEFAULT","conditionValue":0,"direction":"",
               "goods":[],"name":name,"preferentialLimitation":"DEFAULT","receiveLimitation":1,
               "storeId":"1514e1d61686438f95fa46f19070c126","type":"DEDUCTION","validityNumber":"1000",
               "validityPeriod":[],"validityType":"ARRIVED","value":1,
               "inventory":-1,"launchNumber":-1,"status":"AVAILABLE",
               "createrId":"4df73928f8664acfb84da8a62e99fedc","createTime":1660446234000,
               "updateTime":1660446233000,"version":0,"receivedCount":0,"usedCount":0,
               "launchedTimes":1,
               }

        res =self.s.post(self.url,json=data,proxies=self.proxies, verify=False).json()
        return res


if __name__ == '__main__':
    from  case.api.getSession import getSession
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    s=getSession(host,proxies)
    name=None
    res=GetCounponadd(s=s,host=host,proxies=proxies).getCounponadd(name=name)
    print(res['comment'])



