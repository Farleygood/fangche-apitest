#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import unittest
from model.log import logger
from common.read_sql import *
import requests, os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class testLogin(unittest.TestCase):

    def setUp(self):
        pass

    def test_001(self):
        '''房车登录成功'''
        logger.info('正在读取_%s:test_001...'%os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL','fangche_interface_case', 1)[0]
        body = selectMysql('Request_Data','fangche_interface_case', 1)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['data']['username']
        print(check_point)
        print(r.text)
        assert check_point == '13538152630'
        logger.info("%s:test__001测试结果正在写入数据库..."%os.path.basename(os.path.abspath(__file__)))
        if check_point == '13538152630':
            updataMysql('fangche_interface_case',r.text, 'pass','房车登录')
        else:
            updataMysql('fangche_interface_case',r.text, 'fail', '房车登录')
        logger.info('%s:test_001执行完毕.'%os.path.basename(os.path.abspath(__file__)))

    def test_002(self):
        '''房车登录失败,密码错误'''
        logger.info('正在读取_%s:test_002...'%os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL','fangche_interface_case', 7)[0]
        body = selectMysql('Request_Data','fangche_interface_case', 7)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['msg']
        print(check_point)
        print(r.text)
        assert check_point == u'用户名/密码错误'
        logger.info("%s:test__002测试结果正在写入数据库..."%os.path.basename(os.path.abspath(__file__)))
        if check_point == u'用户名/密码错误':
            updataMysql('fangche_interface_case',r.text, 'pass','房车登录失败,密码错误')
        else:
            updataMysql('fangche_interface_case',r.text, 'fail', '房车登录失败,密码错误')
        logger.info('%s:test_002执行完毕.'%os.path.basename(os.path.abspath(__file__)))

    def test_003(self):
        '''房车登录失败,用户名不存在'''
        logger.info('正在读取_%s:test_003...'%os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL','fangche_interface_case', 8)[0]
        body = selectMysql('Request_Data','fangche_interface_case', 8)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['msg']
        print(check_point)
        print(r.text)
        assert check_point == u'用户名/密码错误'
        logger.info("%s:test__003测试结果正在写入数据库..."%os.path.basename(os.path.abspath(__file__)))
        if check_point == u'用户名/密码错误':
            updataMysql('fangche_interface_case',r.text, 'pass','房车登录失败,用户名不存在')
        else:
            updataMysql('fangche_interface_case',r.text, 'fail', '房车登录失败,用户名不存在')
        logger.info('%s:test_003执行完毕.'%os.path.basename(os.path.abspath(__file__)))


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()