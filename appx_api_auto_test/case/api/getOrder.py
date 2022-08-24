import urllib3
urllib3.disable_warnings()
# 获取订单信息
class  GetOrder:

    def __init__(self,s,host,proxies=None):
        self.s=s
        self.host=host
        self.proxies=proxies
        self.url=self.host+'/sc/shop/getDetails'
    def getOrder(self,ids_0):
    # 获取订单信息
        data ={"ids":ids_0}
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
    ids_1=["b9fd1c01d81f49a5a50013aceabc26a2"]
    res=GetOrder(s=s,host=host,proxies=proxies).getOrder(ids_0=ids_1)
    print(res['code'])



