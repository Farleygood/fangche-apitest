#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import unittest
from common.read_excel import *
from common.read_sql import *
import requests,json
from model.log import logger

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class upLoadFile(unittest.TestCase):

    def setUp(self):
        pass

    def test_001(self):
        '''图片上传成功'''
        logger.info('正在读取_{0}:test_001...'.format(os.path.basename(os.path.abspath(__file__))))
        url = selectMysql('Requst_URL','chemi_interface_case', 5)[0]
        # file = str(selectMysql('Request_Data','chemi_interface_case', 5)[0])
        file = {"newfile":open('C:/Users/Public/Pictures/Sample Pictures/1447007795_9803.jpg', 'rb')}
        r = requests.post(url=url, files=file)
        responds = r.json()
        check_point = responds['code']
        print(check_point)
        print(r.text)
        assert check_point == "200"
        logger.info("%s:test__001测试结果正在写入数据库..."%os.path.basename(os.path.abspath(__file__)))
        if check_point == "200":
            updataMysql('chemi_interface_case',r.text, 'pass', '图片上传')
        else:
            updataMysql('chemi_interface_case',r.text, 'fail', '图片上传')
        logger.info('%s:test_001执行完毕.'%os.path.basename(os.path.abspath(__file__)))

    def tearDown(self):
        pass

if __name__ == '__main':
    it = upLoadFile()
    it.test_001()