import sys
import os
import requests
import pytest
import urllib3
urllib3.disable_warnings()

pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pro_path)

from case.api.loginApi import PcLogin

s = requests.session()
host = 'https://backstageservices.dreawer.com'
proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888'
}
pc_login = PcLogin(s=s,host=host,proxies=proxies)


@pytest.mark.parametrize('phoneNumber,password',[('15527060286','hbc23687')])
def test_login_sucess(phoneNumber,password):
    '''正确的用户名、正确的密码，正常登录'''
    res = pc_login.login(phoneNumber=phoneNumber,password=password)
    assert res['code']=='000000'
    assert res['comment']=='Completed successfully'


@pytest.mark.parametrize('phoneNumber,password',[('15527060286','hbc23687111')])
def test_login_file_00(phoneNumber,password):
    '''正确的用户名、错误的密码，登录失败'''
    res = pc_login.login(phoneNumber=phoneNumber,password=password)
    assert res['code']=='114000'
    assert res['comment']=='业务检查错误'

@pytest.mark.parametrize('phoneNumber,password',[('','hbc23687111'),('15527060286','')])
def test_login_file_01(phoneNumber,password):
    '''用户名或密码为空，登录失败'''
    res = pc_login.login(phoneNumber=phoneNumber, password=password)
    assert res['code'] == '113000'
    assert res['comment'] == '输入检查错误'

@pytest.mark.parametrize('phoneNumber,password',[('15527060286111','hbc23687111')])
def test_login_file_02(phoneNumber,password):
    '''不存在的用户名，登录失败'''
    res = pc_login.login(phoneNumber=phoneNumber, password=password)
    assert res['code'] == '114042'
    assert res['comment'] == '数据不存在'




