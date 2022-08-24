import urllib3
urllib3.disable_warnings()
# 通过名称筛选条件查询优惠券
class  GetQueryCounpon:
    def __init__(self,s,host,proxies=None):
        self.s=s
        self.host=host
        self.proxies=proxies
        self.url=self.host+'/mc/business/coupon/getCoupons'

    def getQueryCounpon(self,name,pageNo=1,pageSize=10):

        # 查询名叫"luoyang"优惠卷

        data ={"name":name,"pageInfo":{"pageNo":pageNo,"pageSize":pageSize}}
        proxies = {
            'http': 'http://127.0.0.1:8888',
            'https': 'http://127.0.0.1:8888'
        }
        res =self.s.post(self.url,json=data,proxies=self.proxies, verify=False).json()
        return res
if __name__ == '__main__':
    from case.api.getSession import getSession

    host = 'https://backstageservices.dreawer.com'
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    s=getSession(host,proxies)
    name=None
    res=GetQueryCounpon(s=s,host=host,proxies=proxies).getQueryCounpon(name=name)
    print(res['data']['pageInfo']['totalCount'])
