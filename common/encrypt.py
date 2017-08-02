#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import hashlib
from pyDes import *
import base64
import json

class Enctypt(object):

    def __init__(self):
        # self.codestr = codestr
        pass

    # hash加密
    @staticmethod
    def hash_encode(codestr):
        sha1 = hashlib.sha1()
        sha1.update(codestr.encode('utf-8'))
        # print(sha1.hexdigest())
        return sha1.hexdigest()

    # des加密
    @staticmethod
    def des_encode(codestr, des_key='secretK$'):   # Des_key只能是8的整数倍
        k = des(des_key, padmode=PAD_PKCS5)
        encodeStr = base64.b64encode(k.encrypt(json.dumps(codestr)))
        # print(encodeStr)
        return encodeStr

    # MD5加密
    @staticmethod
    def md5_encode(codestr):
        md5 = hashlib.md5()
        md5.update(codestr.encode('utf-8'))
        print(md5.hexdigest())
        return md5.hexdigest()

if __name__ == "__main__":

    Enctypt.hash_encode("password")
    Enctypt.des_encode("password")

    Enctypt.md5_encode("password")