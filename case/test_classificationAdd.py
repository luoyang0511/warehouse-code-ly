import os
import sys
import requests
import pytest
import urllib3
urllib3.disable_warnings()
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from case.test_classificationDelete import ClassificationDelete
from case.uploadImage import UploadImage
from common.read_yaml import readyml
from common.operation_mysql import execute_sql

yamlPath = os.path.dirname(__file__) + '/caseData/classificationAdd.yml'
data = readyml(yamlPath)


class ClassificationAdd():
    def __init__(self, s, host):
        self.s = s
        self.host = host
        self.url = host+'/gc/classification/add'


    def classificationAdd(self,name,
                          parentId,
                          status,
                          source,
                          sequence=None,
                          logo=None,
                          introduction=None,
                          url=None,
                          recommend=None,
                          remark=None,
                          proxies=None):
        data = {
            'name':name,
            'parentId':parentId,
            'sequence':sequence,
            'logo':logo,
            'introduction':introduction,
            'status':status,
            'url':url,
            'recommend':recommend,
            'remark':remark,
            'source':source,
        }
        r = self.s.post(url=self.url,json=data,verify=False,proxies=proxies).json()
        return r

class TestClassificationAdd():

    @pytest.fixture(scope='module')
    def start_up(self,getSession,getHostAndProxies):
        s = getSession
        host,proxies = getHostAndProxies
        add = ClassificationAdd(s, host)
        file_path = './../image/image.png'
        image = UploadImage(s,host)
        path = image.getImagePath(file_path,proxies=proxies)
        dele = ClassificationDelete(s,host)
        return s,add,path,dele,proxies

    @pytest.fixture(scope='function')
    def db_delete(self,getDbInfo):
        db = getDbInfo
        sql = '''
        DELETE from classification_add where classification_name='{name}'
        '''.format(name=data['classificationAddCase1']['name'])
        execute_sql(db,sql)
        print('删除添加的数据')

    case1_data = data['classificationAddCase1']
    @pytest.mark.parametrize('source',case1_data['source'])
    @pytest.mark.parametrize('status',case1_data['status'])
    @pytest.mark.parametrize('name',case1_data['name'])
    @pytest.mark.parametrize('parentId',case1_data['parentId'])
    def test_classificationAdd(self,start_up,name,parentId,status,source,db_delete):
        '''只传必填项，添加成功'''
        try:
            s,add,path,dele,proxies = start_up
            data = {
                'name':name,
                'parentId':parentId,
                'status':status,
                'source':source,
                'proxies': proxies
            }
            r = add.classificationAdd(**data)
            assert r['code'] == '000000'
            assert r['data'] != None
            classificationId = r['data']
            r = dele.classificationDelete(classificationId,proxies=proxies)
            assert r['code'] == '000000'
        finally:
            db_delete

    case2_data = data['classificationAddCase2']
    @pytest.mark.parametrize('source',case1_data['source'])
    @pytest.mark.parametrize('status',case1_data['status'])
    @pytest.mark.parametrize('name',case1_data['name'])
    @pytest.mark.parametrize('parentId',case1_data['parentId'])
    def test_classificationAdd_uploadImage(self,start_up,name,parentId,status,source):
        '''添加分类，上传图片'''
        s, add, path, dele,proxies = start_up
        data = {
            'name':name,
            'parentId':parentId,
            'status':status,
            'source':source,
            'proxies': proxies,
            'logo':path
        }
        r = add.classificationAdd(**data)
        assert r['code'] == '000000'
        assert r['data'] != None
        classificationId = r['data']
        r = dele.classificationDelete(classificationId,proxies=proxies)
        assert r['code'] == '000000'




# if __name__ == '__main__':
#     from case.getSession import getSession
#     host = 'https://backstageservices.dreawer.com'
#     proxies = {
#         "http": "http://127.0.0.1:8888",
#         "https": "http://127.0.0.1:8888",
#     }
#     s = getSession(host=host,proxies=proxies)
#     add = ClassificationAdd(s,host)
#     data = {
#         'name': 'coco',
#         'parentId': '0',
#         'status': 'DEFAULT',
#         'source': 'RETAIL',
#         'proxies':proxies
#     }
#     r = add.classificationAdd(**data)
#     print(r)

