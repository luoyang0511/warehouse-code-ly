import yaml

import os

import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# from common.mylogger import logger

def readyml(yamlPath):

    '''读取yaml文件内容

    yamlPath: 文件的绝对路径 '''

    if not os.path.isfile(yamlPath):

        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)

    # logger.info('读取的文件路径为：%s'%yamlPath)

    f = open(yamlPath, 'r', encoding='utf-8')

    cfg = f.read()

    data = yaml.load(cfg, Loader=yaml.FullLoader )

    return data

if __name__ == '__main__':
    curPath = os.path.dirname(os.path.dirname(__file__))
    yamlPath=os.path.dirname(os.path.dirname(__file__))+'/conf.yml'
    data=readyml(yamlPath)
    print(data)
    host=data['host']
    print(host)
    proxies=data['proxies']
    print(proxies)
    classificationAddCase=data['classificationAddCase']
    print(classificationAddCase)
