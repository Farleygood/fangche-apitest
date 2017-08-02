#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import requests

def r_uuid():

    url = 'http://rv.huacherv.com/rvcamp/m/user/login/general'
    data = {
            "username":"13538152630",
            "password":"1234567"
            }

    r = requests.post(url,json=data)
    response = r.json()
    uuid = response["data"]["uuid"]
    uid = response["data"]["id"]
    return uuid,uid

if __name__ == '__main__':
    print "uuid:",r_uuid()[0]
    print "uid:",r_uuid()[1]
