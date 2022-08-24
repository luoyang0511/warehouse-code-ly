import pytest
from case.api.getSession import getSession
from case.api.getCounponadd import GetCounponadd

host = 'https://backstageservices.dreawer.com'
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}
s = getSession(host, proxies)

getCounponadd=GetCounponadd(s=s, host=host, proxies=proxies)


#新增复制优惠券

#传入新增的名称
name='luoyang1'
@pytest.mark.parametrize('name',[name])
def test_getCounponadd01(name):
    res=getCounponadd.getCounponadd(name=name)
    assert res['data']['name']==name

#必填的名称字段不传值
name=None
@pytest.mark.parametrize('name',[name])
def test_getCounponadd02(name):
    res=getCounponadd.getCounponadd(name=name)
    assert res['comment']=='为空值'
