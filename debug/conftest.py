import pytest
@pytest.fixture(scope='package')
def login_fix():
    print('执行登录函数')
