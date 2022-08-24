import sys
import os
import requests
import pytest
import urllib3
urllib3.disable_warnings()

pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pro_path)

from case.api.loginApi import PcLogin
from case.api.getUserToken import GetUserToken
from case.api.getUserInfo import GetUserInfo
from case.api.getSession import getSession

s = getSession()







