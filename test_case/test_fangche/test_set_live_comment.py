#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import unittest
from common.read_sql import *
import requests, os
from model.log import logger

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class setLiveComment(unittest.TestCase):

    def setUp(self):
        pass

    def test_001(self):
        '''直播评论'''
        logger.info('正在读取_%s:test_001...'%os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL','fangche_interface_case', 5)[0]
        body = selectMysql('Request_Data','fangche_interface_case', 5)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['msg']
        print(check_point)
        print(r.text)
        assert check_point == u'执行成功'
        logger.info("%s:test__001测试结果正在写入数据库..."%os.path.basename(os.path.abspath(__file__)))
        if check_point == '执行成功':
            updataMysql('fangche_interface_case',r.text, 'pass', '直播评论')
        else:
            updataMysql('fangche_interface_case',r.text, 'fail', '直播评论')
        logger.info('%s:test_001执行完毕.'%os.path.basename(os.path.abspath(__file__)))

    def test_002(self):
        '''直播评论_用户不存在'''
        logger.info('正在读取_%s:test_002...' % os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL', 'fangche_interface_case', 15)[0]
        body = selectMysql('Request_Data', 'fangche_interface_case', 15)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['msg']
        print(check_point)
        print(r.text)
        assert check_point == u'请重新登陆'
        logger.info("%s:test__002测试结果正在写入数据库..." % os.path.basename(os.path.abspath(__file__)))
        if check_point == u'请重新登陆':
            updataMysql('fangche_interface_case', r.text, 'pass', '直播评论_用户不存在')
        else:
            updataMysql('fangche_interface_case', r.text, 'fail', '直播评论_用户不存在')
        logger.info('%s:test_002执行完毕.' % os.path.basename(os.path.abspath(__file__)))

    def tearDown(self):
        pass

if __name__ == '__main':
    it = setLiveComment()
    it.test_001()