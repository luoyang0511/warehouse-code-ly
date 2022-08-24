import pytest

# 单个参数单个值
# @pytest.mark.parametrize('phoneNumber',['1837474623'])
# def test_login(phoneNumber):
#     print('\n',phoneNumber)

# # 单个参数多个值
# @pytest.mark.parametrize('status',[1,2,3,4,5])
# def test_02(status):
#     print(status)

# 多个参数单个值
# @pytest.mark.parametrize('phoneNumber,password',[('15527060286','hbc23687')])
# def test_03(phoneNumber,password):
#     print(phoneNumber)
#     print(password)

# 多个参数多个值
# @pytest.mark.parametrize('phoneNumber,password',[('','12345'),('1283473','')])
# def test_04(phoneNumber,password):
#     print(phoneNumber)
#     print(password)

# 笛卡尔积
@pytest.mark.parametrize('phoneNumber',['coco','zhangsan'])
@pytest.mark.parametrize('password',['12345','7890'])
def test_05(phoneNumber,password):
    print(phoneNumber)
    print(password)

@pytest.mark.parametrize('user',['coco','中文','123','coco123'])
@pytest.mark.parametrize('status',[1,2,3,4,5])
def test_02(user,status):
    print(status)
