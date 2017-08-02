#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'


'''
没用的文件,先放到这里
'''

import xlrd
import xlwt
import json
from common.read_sql import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


'''
work_file = xlrd.open_workbook(r'C:\\Users\\Administrator\\Desktop\\InterfaceTestCasetemplate.xlsx')
work_sheet = work_file.sheet_by_index(0)

work_cell51 = work_sheet.cell(5, 1).value
work_cell52 = work_sheet.cell(5, 2).value

cell51_to_json = json.loads(work_cell51)
cell52_to_json = json.loads(work_cell52)
'''
# copy_file = copy(work_file)
# copy_sheet = copy_file.get_sheet(0)

def write_excle(agr):
    write_file = xlwt.Workbook(encoding='utf-8')
    write_sheet = write_file.add_sheet('sheet1', cell_overwrite_ok=True)
    write_sheet.write(5, 4, agr)
    write_file.save('interface.xls')

def check_point_assert(tid,API_Pru):
    check_value = json.loads(selectMysql('Check_Point',tid=tid))
    response_value = json.loads(selectMysql('Response',tid=tid))
    check_value_of_key = []
    check_value_of_value = []
    response_value_of_key = []
    response_value_of_value = []

    # check_point
    for k,v in check_value.items():
        if isinstance(v, list):
            for i in v:
                for ki,vi in i.items():
                    check_value_of_key.append(ki)
                    check_value_of_value.append(vi)
        check_value_of_key.append(k)
        check_value_of_value.append(v)

    # response
    for k1, v1 in response_value.items():
        if isinstance(v1, list):
            for i in v1:
                for ki, vi in i.items():
                    response_value_of_key.append(ki)
                    response_value_of_value.append(vi)
        response_value_of_key.append(k1)
        response_value_of_value.append(v1)

    # 判断check_point的key和value是否在response里面,在Result里则写入pass,否则写入fail
    for i in range(len(response_value_of_key)):
        if response_value_of_key[i] in check_value_of_key and response_value_of_value[i] in check_value_of_value:
            if i == len(response_value_of_key) - 1:
                # write_excle('pass')
                updata_result("pass",API_Pru)
                return True
        else:
            # write_excle('''fail:\nreason: {"%s":"%s"}''' % (k52[i], v52[i]))
            updata_result("fail: reason:{'%s':'%s'}",API_Pru) %(response_value_of_key[i],response_value_of_value[i])
            return False
            break

if __name__ == '__main__':
    # a = check_point_assert(2,'检测新版本')
    a = selectMysql('Check_Point', tid=2)
    # check_value = dict(selectMysql('Check_Point', tid=2))
    # print check_value
    # print type(check_value)
    print a
    print type(a)
    print isinstance(a,str)

'''
k51 = []
v51 = []
k52 = []
v52 = []

# check_point
for k,v in cell51_to_json.items():
    if isinstance(v, list):
        for i in v:
            for ki,vi in i.items():
                k51.append(ki)
                v51.append(vi)
    k51.append(k)
    v51.append(v)

# response
for k1,v1 in cell52_to_json.items():
    if isinstance(v1, list):
        for i in v1:
            for ki,vi in i.items():
                k52.append(ki)
                v52.append(vi)
    k52.append(k1)
    v52.append(v1)

# 判断check_point的key和value是否在response里面,在Result里则写入pass,否则写入fail
for i in range(len(k52)):
    if k52[i] in k51 and v52[i] in v51:
        if i == len(k52) - 1:
            write_excle('pass')
    else:
        write_excle('fail:\nreason: {"%s":"%s"}' %(k52[i],v52[i]))
        break

print k51
print k52
print v51
print v52

'''