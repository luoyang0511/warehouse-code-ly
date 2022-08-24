import urllib3
urllib3.disable_warnings()


class GetGoods():

    def __init__(self,s,host,proxies=None):
        self.s = s
        self.host = host
        self.proxies = proxies
        self.url = self.host+'/gc/goods/getDetails'

    def getgoods(self,storeId,status='DEFAULT',pageNo=1,pageSize=10):
        data={"storeId":storeId,
              "status":status,
              "pageInfo":
                  {"pageNo":pageNo,
                   "pageSize":pageSize}
              }
        res =self.s.post(self.url, json=data, proxies=self.proxies, verify=False).json()
        return res

if __name__ == '__main__':
    from case.api.getSession import getSession
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888'
    }
    s = getSession(host,proxies=proxies)
    # storeId='1514e1d61686438f95fa46f19070c126'
    storeId=None
    res = GetGoods(s=s, host=host, proxies=proxies).getgoods(storeId=storeId)
    print(res)
    # print(res['code']['pageInfo']['totalPage'])

