import  pytest
'''

@pytest.mark.parametrize('username',['coco','zhangsan','lisi'])
def test_login(username):
    print('username:%s'%username)

@pytest.mark.parametrize('luo',[0,1,2,3])
def test_login01(luo):
    print('luo%s'%luo)

@pytest.mark.parametrize('phone,code',[('15972939000','1234')])
def test_login02(phone,code):
    print('phone%s'%phone)
    print('code%s'%phone)
'''
@pytest.mark.parametrize('username01',['luo','yang'])
@pytest.mark.parametrize('pwd01',['123','456'])
def test_login03(username01,pwd01):
    print('username01%s'%username01)
    print('pwd01%s'%pwd01)