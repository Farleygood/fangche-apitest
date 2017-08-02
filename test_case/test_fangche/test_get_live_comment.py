#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import unittest
from common.read_sql import *
import requests, os
from model.log import logger
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class getComment(unittest.TestCase):

    def setUp(self):
        updata_tables('chemi_interface_case', '', '')

    def test_001(self):
        '''获取直播评论列表'''
        logger.info('正在读取_%s:test_001...'%os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL','fangche_interface_case', 2)[0]
        body = selectMysql('Request_Data','fangche_interface_case', 2)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['code']
        print(check_point)
        print(r.text)
        assert check_point == 200
        logger.info("%s:test__001测试结果正在写入数据库..."%os.path.basename(os.path.abspath(__file__)))
        if check_point == 200:
            updataMysql('fangche_interface_case',r.text, 'pass', '获取直播评论列表')
        else:
            updataMysql('fangche_interface_case',r.text, 'fail', '获取直播评论列表')
        logger.info('%s:test_001执行完毕.'%os.path.basename(os.path.abspath(__file__)))

    def test_002(self):
        '''获取直播评论列表失败'''
        logger.info('正在读取_%s:test_002...' % os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL', 'fangche_interface_case', 9)[0]
        body = selectMysql('Request_Data', 'fangche_interface_case', 9)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['msg']
        print(check_point)
        print(r.text)
        assert check_point == u'操作失败'
        logger.info("%s:test__002测试结果正在写入数据库..." % os.path.basename(os.path.abspath(__file__)))
        if check_point == u'操作失败':
            updataMysql('fangche_interface_case', r.text, 'pass', '获取直播评论列表失败')
        else:
            updataMysql('fangche_interface_case', r.text, 'fail', '获取直播评论列表失败')
        logger.info('%s:test_002执行完毕.' % os.path.basename(os.path.abspath(__file__)))

    def test_003(self):
        '''获取直播评论列表失败'''
        logger.info('正在读取_%s:test_003...' % os.path.basename(os.path.abspath(__file__)))
        url = selectMysql('Requst_URL', 'fangche_interface_case', 10)[0]
        body = selectMysql('Request_Data', 'fangche_interface_case', 10)[0]
        r = requests.post(url=url, data=body)
        responds = r.json()
        check_point = responds['msg']
        print(check_point)
        print(r.text)
        assert check_point == u'操作失败'
        logger.info("%s:test__003测试结果正在写入数据库..." % os.path.basename(os.path.abspath(__file__)))
        if check_point == u'操作失败':
            updataMysql('fangche_interface_case', r.text, 'pass', '获取直播评论列表失败')
        else:
            updataMysql('fangche_interface_case', r.text, 'fail', '获取直播评论列表失败')
        logger.info('%s:test_003执行完毕.' % os.path.basename(os.path.abspath(__file__)))

    def tearDown(self):
        pass

if __name__ == '__main':
    it = getComment()
    it.test_001()
