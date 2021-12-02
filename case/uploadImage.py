import os
import sys
import requests
import urllib3
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class UploadImage():
    def __init__(self,s,host):
        self.s = s
        self.host= host
        self.url = host+'/ic/uploadImage'

    def uploadImage(self,file_path,proxies=None):
        file_name = os.path.split(file_path)[1]
        data = {
            'appname':'RETAIL',
            'type':'IMAGE'
        }
        files = {
            'file':(file_name,open(file_path,'rb'),'image/jpeg')
        }
        r = self.s.post(url=self.url,data=data,files=files,proxies=proxies,verify=False).json()
        return r

    def getImagePath(self,file_path,proxies=None):
        r = self.uploadImage(file_path,proxies)
        image_path = r['data'][0]
        return image_path

if __name__ == '__main__':
    s = requests.session()
    host = 'https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    file_path = './../image/image.png'
    image = UploadImage(s,host)
    # r = image.uploadImage(host,file_path,proxies=proxies)
    #
    image_path = image.getImagePath(file_path,proxies)
    print(image_path)

# import requests
# def uploadImage(host,proxies=None):
#     url = host+'/ic/uploadImage'
#
#     data = {
#         'appname':'RETAIL',
#         'type':'IMAGE'
#     }
#     files = {
#         'file':('image.png',open('./../image/image.png','rb'),'image/jpeg')
#     }
#
#     r = requests.post(url=url,data=data,files=files,proxies=proxies,verify=False)
#     return r
# proxies = {
#     "http": "http://127.0.0.1:8888",
#     "https": "http://127.0.0.1:8888",
# }
# host = 'https://backstageservices.dreawer.com'
# r = uploadImage(host,proxies=proxies)
# print(r.json())