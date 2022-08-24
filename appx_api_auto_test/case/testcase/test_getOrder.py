import pytest
from case.api.getSession import getSession
from case.api.getOrder import GetOrder

host = 'https://backstageservices.dreawer.com'
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}
s = getSession(host, proxies=proxies)

getorder = GetOrder(s=s, host=host, proxies=proxies)

# 断言订单信息
# 1.正确传参
ids_1 = ["b9fd1c01d81f49a5a50013aceabc26a2"]
@pytest.mark.parametrize('ids_0',ids_1)
def test_getOrder01(ids_0):
    res=getorder.getOrder(ids_0=ids_1)
    assert res['data'][0]['address']=='百家乐园生活'

# # 2.错误传参
ids_2 = [ "b9fd1c01d81f49a5a500"]
@pytest.mark.parametrize('ids_0',ids_2)
def test_getOrder02(ids_0):
    res=getorder.getOrder(ids_0=ids_2)
    assert res['comment']=='Completed successfully'

#
# # 3.空值传参
@pytest.mark.parametrize('ids_0',[''])
def test_getOrder03(ids_0):
    res=getorder.getOrder(ids_0=ids_0)
    assert res['status']==400

# 4.不传参
ids_4=None
@pytest.mark.parametrize('ids_0',[ids_4])
def test_getOrder04(ids_0):
    res=getorder.getOrder(ids_0=ids_0)
    assert res['comment']=='输入检查错误'

