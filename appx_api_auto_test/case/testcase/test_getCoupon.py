import pytest
from case.api.getSession import getSession
from case.api.getCoupon import GetCounpon
host = 'https://backstageservices.dreawer.com'
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}
s = getSession(host, proxies=proxies)
counpon=GetCounpon(s=s,host=host,proxies=proxies)


#请求优惠卷列表
# # 正确的传参
@pytest.mark.parametrize('pageNo,pageSize',[('1','10')])
def test_getCounpon01(pageNo,pageSize):
  res=counpon.getCounpon(pageNo=pageNo,pageSize=pageSize)
  assert res['data']['coupons'][0]['value']==1

# 传空传参
pageNo=None
pageSize=None
@pytest.mark.parametrize('pageNo,pageSize',[(pageNo,pageSize)])
def test_getCounpon02(pageNo,pageSize):
  res=counpon.getCounpon(pageNo=pageNo,pageSize=pageSize)
  assert res['data']['coupons'][0]['value']==1

