#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import unittest
from common.read_excel import *
from common.read_sql import *
import requests
from model.log import logger
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class getVersion(unittest.TestCase):

    def setUp(self):
        pass

    @unittest.skipIf(selectMysql('Active'==1,'chemi_interface_case',1),"Active == 1时跳过此用例")
    def test_001(self):
        '''获取720设备最新版本'''
        logger.info('正在读取_%s:test_001...'%os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL','chemi_interface_case',1)[0]
        body = selectMysql('Request_Data','chemi_interface_case',1)[0]
        r = requests.post(url=url,data=body)
        responds = r.json()
        check_point = responds['msg']
        print(check_point)
        print(r.text)
        assert check_point == u'执行成功'
        logger.info("%s:test__001测试结果正在写入数据库..."%os.path.basename(os.path.abspath(__file__)))
        if check_point == '执行成功':
            updataMysql('chemi_interface_case',r.text, 'pass','获取720设备最新版本')
        else:
            updataMysql('chemi_interface_case',r.text, 'fail', '获取720设备最新版本')
        logger.info('%s:test_001执行完毕.'%os.path.basename(os.path.abspath(__file__)))

    def test_002(self):
        '''获取720_53设备最新版本'''
        logger.info('正在读取_%s:test_002...'%os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL','chemi_interface_case', 3)[0]
        body = selectMysql('Request_Data','chemi_interface_case', 3)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['msg']
        print(check_point)
        print(r.text)
        assert check_point == u'执行成功'
        logger.info("%s:test__002测试结果正在写入数据库..."%os.path.basename(os.path.abspath(__file__)))
        if check_point == '执行成功':
            updataMysql('chemi_interface_case',r.text, 'pass','获取720_53设备最新版本')
        else:
            updataMysql('chemi_interface_case',r.text, 'fail', '获取720_53设备最新版本')
        logger.info('%s:test_002执行完毕.'%os.path.basename(os.path.abspath(__file__)))

    def test_003(self):
        '''获取720can设备最新版本'''
        logger.info('正在读取_%s:test_003...'%os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL','chemi_interface_case', 4)[0]
        body = selectMysql('Request_Data','chemi_interface_case', 4)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['code']
        print(check_point)
        print(r.text)
        assert check_point == 200
        logger.info("%s:test__003测试结果正在写入数据库..."%os.path.basename(os.path.abspath(__file__)))
        if check_point == 200:
            updataMysql('chemi_interface_case',r.text, 'pass', '获取720can设备最新版本')
        else:
            updataMysql('chemi_interface_case',r.text, 'fail', '获取720can设备最新版本')
        logger.info(u'正在生成测试报告...')
        logger.info('%s:test_003执行完毕.'%os.path.basename(os.path.abspath(__file__)))

    def tearDown(self):
        pass

if __name__ == '__main':
    it = getVersion()
    it.test_001()
    it.test_002()
    it.test_003()
