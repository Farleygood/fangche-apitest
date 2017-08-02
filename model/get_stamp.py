#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import httplib
import time
import datetime
import os

# 当脚本在本地跑的时候用来获取服务器的时间戳,用来计算token
def get_webservertime(host):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("GET","/")
        r = conn.getresponse()
        ts = r.getheader("date")  #GMT时间
        print ts
        dt = datetime.datetime.strptime(ts,'%a, %d %b %Y %H:%M:%S GMT')
        st = time.mktime(dt.timetuple())
        print st
    except Exception as e:
        return e

get_webservertime('127.0.0.1')

# print time.mktime(datetime.datetime.now().timetuple())