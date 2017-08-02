#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import xlrd
import os
import json
from model.log import logger

# 读取单元格
def readFile(rowValue, colValue):
    # 读取request data
    try:
        logger.info(u"正在读取测试用例...")
        work_book = xlrd.open_workbook(os.path.join(os.path.dirname(os.getcwd()), "Data_Driven\\InterfaceTest.xlsx"))
        work_sheet = work_book.sheet_by_index(0)
        # cell_value = work_sheet.cell_value(rowValue, colValue)
        cell_value = work_sheet.cell(rowValue,colValue).value.encode('utf-8').replace('\r','').replace('\n','')

    except Exception as e:
        return e
    return cell_value

# 获取用例的行数
def read_lines():
    try:
        work_book = xlrd.open_workbook(os.path.join(os.path.dirname(os.getcwd()), "Data_Driven\\InterfaceTest.xlsx"))
        work_sheet = work_book.sheet_by_index(0)
        rows = work_sheet.nrows
    except Exception as e:
        return e
    return rows

# 获取host
def getHost(rowValue, colValue):
    try:
        work_book = xlrd.open_workbook(os.path.join(os.path.dirname(os.getcwd()), "Data_Driven\\InterfaceTest.xlsx"))
        work_sheet = work_book.sheet_by_index(0)
        cell_value = work_sheet.cell(rowValue, colValue).value.encode('utf-8').replace('\r','').replace('\n','')
    except Exception as e:
        return e
    return cell_value

# 拼接url ==>host+apiurl
def getUrl(row,apiHost=2,apiUrl=3):
    # 拼接url
    try:
        if row < 1:
            return u"row不能小于1"
        else:
            logger.info(u"正在拼接url...")
            url = getHost(row,apiHost) + getHost(row,apiUrl)
    except Exception as e:
        return e
    return url

if __name__ == "__main__":
    cell16 = readFile(1, 6)
    # print(type(cell16))
    cell16_1 = readFile(1,7)
    # j = json.dumps(cell16_1)
    print(type(cell16_1))

    # print(type(cell16))
    # url = getUrl(3)
    # print(url)