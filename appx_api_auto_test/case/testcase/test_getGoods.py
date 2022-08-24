import pytest
from case.api.getGoods import GetGoods
from case.api.getSession import getSession

host = 'https://backstageservices.dreawer.com'
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}
s = getSession(host=host,proxies=proxies)
goods = GetGoods(s=s,host=host,proxies=proxies)
# 商品信息列表断言

# 传入正确的值
@pytest.mark.parametrize('storeId',['1514e1d61686438f95fa46f19070c126'])
def test_getGoods01(storeId):
    res = goods.getgoods(storeId=storeId)
    assert res['data']['goodses'][0]['name'] == '桀桀桀1'

# 传入错误的值
@pytest.mark.parametrize('storeId',['1514e1d61686438f95fa46f1'])
def test_getGoods02(storeId):
    res = goods.getgoods(storeId=storeId)
    assert res['data']['pageInfo']['totalPage']== 0


# # 传入空的值
@pytest.mark.parametrize('storeId',[''])
def test_getGoods03(storeId):
    res = goods.getgoods(storeId=storeId)
    assert res['code'] == '113000'
    assert res['comment'] == '输入检查错误'

# # 必填参数不填
@pytest.mark.parametrize('storeId',[None])
def test_getGoods04(storeId):
    res = goods.getgoods(storeId=storeId)
    assert res['data'] == None
    assert res['comment'] == '输入检查错误'
