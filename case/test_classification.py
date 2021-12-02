import  requests
import  os
import  pytest
import  urllib3

from case.uploadImage import UploadImage
from case.test_classificationDelete import ClassificationDelete
class  ClassificationAdd():
    def __init__(self,s,host):
        self.s=s
        self.host=host
        self.url=host+'/gc/classification/add'

    def  classification(self,name,parentId,status,source,proxies=None):
        data={
                "name":name,
                "parentId":parentId,
                "status":status,
                "source":source
        }
        r=self.s.post(url=self.url,json=data,proxies=proxies,verify=False).json()
        return  r



class TestClassificationAdd():
    host='https://backstageservices.dreawer.com'
    proxies = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888",
    }
    @pytest.fixture(scope='module')
    def start_up(self,getSession):
        s=getSession

        add = ClassificationAdd(s, self.host)
        file_path = './../image/image.png'
        image = UploadImage(s, self.host)
        path = image.getImagePath(file_path, proxies=self.proxies)
        dele = ClassificationDelete(s, self.host)
        return s, add, path, dele

    @pytest.mark.parametrize('source',['RETAIL'])
    @pytest.mark.parametrize('',)
    def test_classificationAdd_uploadImage(self,start_up,name,parentId,status,source):
        s,add,path,dele =start_up
        data={
            'name':name,
            'parentId':parentId,

        }




