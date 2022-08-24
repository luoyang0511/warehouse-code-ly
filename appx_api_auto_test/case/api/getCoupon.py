import urllib3
urllib3.disable_warnings()
#请求优惠卷列表
class GetCounpon:

    def __init__(self,s,host,proxies):
        self.s=s
        self.host=host
        self.proxies=proxies
        self.url=self.host+'/mc/business/coupon/getCoupons'

    def getCounpon(self,pageNo,pageSize):
        data ={"pageInfo":{"pageNo":pageNo,"pageSize":pageSize}}
        res =self.s.post(self.url,json=data, proxies=self.proxies, verify=False).json()
        return res

if __name__ == '__main__':
    from  case.api.getSession import getSession
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    s=getSession(host,proxies=proxies)
    pageNo =None
    pageSize =None
    res=GetCounpon(s=s,host=host,proxies=proxies).getCounpon(pageNo=pageNo,pageSize=pageSize)
    print(res['data']['coupons'][0]['value'])
