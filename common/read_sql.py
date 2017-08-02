#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import MySQLdb
import re

conn=dict(host='127.0.0.1',user='root',passwd='',db='test',charset='utf8')

def selectMysql(tru, tb ,tid):
    try:
        db = MySQLdb.connect(**conn)
        cur = db.cursor()
        cur.execute("select %s from %s where id = %s" % (tru, tb, tid))
        data = cur.fetchone()
    except Exception as e:
        print("请检查数据库连接"),e
    return data
    db.close()

def updataMysql(tb, field1,field2,field3):
    try:
        db = MySQLdb.connect(**conn)
        cur = db.cursor()
    except Exception as e:
        print("请检查数据库连接"),e
    try:
        cur.execute("update %s set Response='%s',Result='%s' WHERE API_Purpose='%s'" %(tb,field1,field2,field3))
        db.commit()
    except Exception as e:
        db.rollback()
        print("更新数据出错"),e
    db.close()

# 初始化时调用,清空Response,Result
def updata_tables(tb, field1,field2):
    try:
        db = MySQLdb.connect(**conn)
        cur = db.cursor()
    except Exception as e:
        print("请检查数据库连接"),e
    try:
        cur.execute("update %s set Response='%s',Result='%s'" %(tb,field1,field2))
        db.commit()
    except Exception as e:
        db.rollback()
        print("更新数据出错"),e
    db.close()

def updata_result(tb,result,desc):
    try:
        db = MySQLdb.connect(**conn)
        cur = db.cursor()
    except Exception as e:
        print("请检查数据库连接"),e
    try:
        cur.execute("update %s set Result='%s' WHERE API_Purpose='%s'" %(tb,result,desc))
        db.commit()
    except Exception as e:
        db.rollback()
        print("更新数据出错"),e
    db.close()

def deleteMysql(tb,field1,field2):

    try:
        db = MySQLdb.connect(**conn)
        cur = db.cursor()
    except Exception as e:
        print("请检查数据库连接"),e
    try:
        cur.execute("delete from %s where %s=%s"% (tb,field1,field2))
        db.commit()
    except Exception as e:
        db.rollback()
        print("删除数据出错"),e
    db.close()

if __name__ == '__main__':
    file = str(selectMysql('Request_Data', 'chemi_interface_case', 5)[0])
    import json
    print json.dumps(file)