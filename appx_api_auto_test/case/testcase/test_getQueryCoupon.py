import  pytest
from case.api.getSession import getSession
from case.api.getQueryCoupon import GetQueryCounpon
host = 'https://backstageservices.dreawer.com'
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}
s = getSession(host, proxies)
# name = 'luoyang'
getQueryCounpon = GetQueryCounpon(s=s, host=host, proxies=proxies)

# 通过名称筛选条件查询优惠券

# 传入已存在的名称进行筛选
name = 'luoyang1'
@pytest.mark.parametrize('name',[name])
def  test_getQueryCoupon01(name):
    res=getQueryCounpon.getQueryCounpon(name=name)
    assert res['data']['coupons'][0]['name']==name


# 模糊查询筛选
name ='luo'
@pytest.mark.parametrize('name',[name])
def  test_getQueryCoupon02(name):
    res=getQueryCounpon.getQueryCounpon(name=name)
    assert res['data']['coupons'][0]['name']=='luoyang1'


 #传入不存在的名称进行筛选
name = 'luoyangxxxx'
@pytest.mark.parametrize('name',[name])
def  test_getQueryCoupon03(name):
    res=getQueryCounpon.getQueryCounpon(name=name)
    assert res['data']['pageInfo']['totalCount']==0


