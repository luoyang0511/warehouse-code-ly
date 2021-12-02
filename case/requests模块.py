import requests
import urllib3
import json
urllib3.disable_warnings()
# url = 'https://backstageservices.dreawer.com/bsmc/user/getInfo'
# proxies = {
#   "http": "http://127.0.0.1:8888",
#   "https": "http://127.0.0.1:8888",
# }
# h = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
#     'appid':'1514e1d61686438f95fa46f19070c126',
#     'Authorization':'f70f826ac5af4cf48d718af5e3d1ea76'
# }
# r = requests.get(url=url,headers=h,verify=False,proxies=proxies)
# 如果url里面有参数，用params=来传参
# url = 'https://backstageservices.dreawer.com/ecmps/getUserToken'
# data = {
#     'appId':'1514e1d61686438f95fa46f19070c126'
# }
# h = {
#     'appid':'1514e1d61686438f95fa46f19070c126',
#     'Authorization':'4a657a152e4e41d6871f4de369200dfc'
# }
# r = requests.get(url=url,params=data,headers=h,verify=False,proxies=proxies)
# print(r.text)


# # http://japi.juhe.cn/qqevaluate/qq?key=8dbee1fcd8627fb6699bce7b986adc45&qq=%E4%B8%AD%E6%96%87
# url = 'http://japi.juhe.cn/qqevaluate/qq'
# key = '8dbee1fcd8627fb6699bce7b986adc45'
# data = {
#     'key':key,
#     'qq':'中文'
# }
#
# r = requests.get(url=url,params=data)
# print(r.text)

# url = 'https://backstageservices.dreawer.com/ecmps/login'
# h = {
#     # 'Content-Type': 'application/json;charset=UTF-8',
#     'appid': '1514e1d61686438f95fa46f19070c126'
# }
# data = {"phoneNumber":"15527060286","password":"hbc23687"}
# # json去传参的时候 第一是帮我们把字典格式的data转化为符合json规则的字符串，第二就是帮我们传了Content-Type：application/json
# r = requests.post(url=url,json=data,headers=h,verify=False,proxies=proxies)
# # r = requests.post(url=url,data=json.dumps(data),headers=h,verify=False,proxies=proxies)

# url = 'http://work.91zhanghu.com/login/webLoginAjax'
# # h = {
# #     'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
# # }
# data = {'userAccount':'13266775912',
#      'passwordMd5':'c8837b23ff8aaa8a2dde915473ce0991'}
# # data=去传参，第一是我们把字典格式的data转化为符合json规则的字符串，第二就是帮我们传了Content-Type：x-www-form-urlencoded
# r = requests.post(url=url,data=data,verify=False,proxies=proxies)

# # 第一种方式 MultipartEncoder
# from requests_toolbelt import MultipartEncoder
# url = 'https://backstageservices.dreawer.com/ic/uploadImage'
# data = {'appname':'RETAIL',
#         'type':'IMAGE',
#         'file':('image.png',open('image.png','rb'),'image/jpeg')}
# data = MultipartEncoder(fields=data)
# h = {'Content-Type':data.content_type}
# requests.post(url=url,data=data,headers=h,verify=False,proxies=proxies)
#
# # 第二种方式
# url = 'https://backstageservices.dreawer.com/ic/uploadImage'
# data = {'appname':'RETAIL',
#         'type':'IMAGE'
#         }
# files = {'file':('image.png',open('image.png','rb'),'image/jpeg')}
# requests.post(url=url,data=data,files=files,verify=False,proxies=proxies)

# image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
# r = requests.get(url=image_url,verify=False,proxies=proxies)
# print(r.content)
# with open('dir1/python_logo.png','wb') as f:
#     f.write(r.content)

# file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
# '''
# stream参数默认情况下是False，它会立即开始下载文件并存放到内存中，倘若文件过大就会导致内存不足
# stream设置为Ture时，它不会立即开始下载，当使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载
# iter_content：一块一块的遍历要下载的内容
# iter_lines：一行一行的遍历要下载的内容
# '''
# r = requests.get(file_url, stream=True,proxies=proxies,verify=False)
# with open("python.pdf", "wb") as pdf:
#     for chunk in r.iter_content(chunk_size=1024):
#         if chunk:
#             pdf.write(chunk)
#

# url = 'https://backstageservices.dreawer.com/ecmps/getUserToken'
# data = {
#     'appId':'1514e1d61686438f95fa46f19070c126'
# }
# h = {
#     'appid':'1514e1d61686438f95fa46f19070c126',
#     'Authorization':'4a657a152e4e41d6871f4de369200dfc'
# }
# r = requests.get(url=url,params=data,headers=h,verify=False,proxies=proxies)
# # print(r)
# # print([type(r.text),r.text])
# # print([type(r.content),r.content])
# # print([type(r.json()),r.json()['data']['token']])
# print(r.headers)
# print(r.status_code)
# print(r.encoding)
# print(r.cookies)


# import json
# dic = {
#     'a':123,
#     'b':88.8,
#     'c':None,
#     'd':True,
#     'e':False,
#     'f':'hello world',
#     'g':(1,2,'你好'),
#     'h':['python',1,True],
#     'i':{
#         'name':'coco',
#         'pwd':123456
#     }
# }
# str_dict = json.dumps(dic)
# print(str_dict)
# new_dic = json.loads(str_dict)
# print(new_dic)
proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888",
}
class Login():
    def login(self,s,host,phoneNumber,password):
        url = host+'/ecmps/login'
        data = {"phoneNumber":phoneNumber,"password":password}
        r = s.post(url=url,json=data,verify=False,proxies=proxies).json()
        return r

    def getTokenAndAppID(self,s,host,phoneNumber='15527060286',password='hbc23687'):
        r = self.login(s,host,phoneNumber,password)
        token = r['data']['token']
        appid = r['data']['apps'][0]['appId']
        return token,appid

class GetUserToken():

    def getUserToken(s,host,appid):
        url = host+'/ecmps/getUserToken'
        data = {'appId':appid}
        r = s.get(url=url,params=data,verify=False,proxies=proxies).json()
        return r



def getSession(host):
    s = requests.session()
    l = Login()
    token,appid = l.getTokenAndAppID(s,host)
    h = {
        'appid':appid,
        'Authorization':token}
    s.headers.update(h)
    r = getUserToken(s,host,appid)
    real_token = r['data']['token']
    h = {'Authorization':real_token}
    s.headers.update(h)
    return s

# s = getSession()
# print(s.headers)

# url = 'https://backstageservices.dreawer.com/bsmc/user/getInfo'
# r = s.get(url=url,verify=False,proxies=proxies).json()
# print(r)
#
# url = 'https://backstageservices.dreawer.com/bsmc/user/getMenu'
# r = s.get(url=url,verify=False,proxies=proxies).json()
# print(r)
if __name__ == '__main__':
    host = 'https://backstageservices.dreawer.com'
    phoneNumber="15527060286"
    password="15527060286"
    s = getSession(host,phoneNumber,password)
    url = 'https://backstageservices.dreawer.com/bsmc/user/getMenu'
    r = s.get(url=url,verify=False,proxies=proxies).json()
    print(r)


