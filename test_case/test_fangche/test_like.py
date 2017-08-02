#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'


import unittest
import os
import requests,re
from common.read_sql import *
from model.log import logger
from login import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class setLike(unittest.TestCase):

    def setUp(self):
        pass

    def test_001(self):
        '''点赞与打赏'''
        logger.info('正在读取_{0}:test_001...'.format(os.path.basename(os.path.abspath(__file__))))
        uid = r_uuid()[1]
        url = selectMysql('Requst_URL', 'fangche_interface_case', 3)[0]
        body = selectMysql('Request_Data', 'fangche_interface_case', 3)[0]
        body = str(body).replace('${id}',uid)
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['code']
        print(check_point)
        print(r.text)
        assert check_point == 200
        logger.info("{0}:test__001测试结果正在写入数据库...".format(os.path.basename(os.path.abspath(__file__))))
        if check_point == 200:
            updataMysql('fangche_interface_case', r.text, 'pass', '点赞与打赏')
        else:
            updataMysql('fangche_interface_case', r.text, 'fail', '点赞与打赏')
        logger.info('{0}:test_001执行完毕.'.format(os.path.basename(os.path.abspath(__file__))))

    def test_002(self):
        '''点赞与打赏,用户不存在/未登陆'''
        logger.info('正在读取_{0}:test_002...'.format(os.path.basename(os.path.abspath(__file__))))
        url = selectMysql('Requst_URL', 'fangche_interface_case', 11)[0]
        body = selectMysql('Request_Data', 'fangche_interface_case', 11)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['msg']
        print(check_point)
        print(r.text)
        assert check_point == u'用户未登录'
        logger.info("{0}:test__002测试结果正在写入数据库...".format(os.path.basename(os.path.abspath(__file__))))
        if check_point == '用户未登陆':
            updataMysql('fangche_interface_case', r.text, 'pass', '点赞与打赏,用户不存在/未登陆')
        else:
            updataMysql('fangche_interface_case', r.text, 'fail', '点赞与打赏,用户不存在/未登陆')
        logger.info('{0}:test_002执行完毕.'.format(os.path.basename(os.path.abspath(__file__))))

    def test_003(self):
        '''点赞与打赏, live_type不正确'''
        logger.info('正在读取_{0}:test_003...'.format(os.path.basename(os.path.abspath(__file__))))
        uid = r_uuid()[1]
        url = selectMysql('Requst_URL', 'fangche_interface_case', 12)[0]
        body = selectMysql('Request_Data', 'fangche_interface_case', 12)[0]
        body = str(body).replace('${id}', uid)
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['msg']
        print(check_point)
        print(r.text)
        assert check_point == u'参数不正确'
        logger.info("{0}:test__003测试结果正在写入数据库...".format(os.path.basename(os.path.abspath(__file__))))
        if check_point == '参数不正确':
            updataMysql('fangche_interface_case', r.text, 'pass', '点赞与打赏,用户不存在/未登陆')
        else:
            updataMysql('fangche_interface_case', r.text, 'fail', '点赞与打赏,用户不存在/未登陆')
        logger.info('{0}:test_003执行完毕.'.format(os.path.basename(os.path.abspath(__file__))))


    def tearDown(self):
        pass

if __name__ == '__main':
    unittest.main()