#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

from read_excel import *
import re

# 匹配所有的要关联的参数,格式${xxx}
def extract_correlation_():
    correlat_ = []
    for i in range(read_lines()-1):
        correlation = re.findall(r'\$\{.+?\}', readFile(i+1,7))
        for j in correlation:
            correlat_.append(j)
    return correlat_

# 匹配所有要关联的字段,格式为${xxxx}中间的xxxx字符串
def extract_correlation():
    correla = []
    for i in range(read_lines()-1):
        corr = re.findall(r'\$\{(\w+)', readFile(i+1,7))
        for j in corr:
            correla.append(j)
    return correla



if __name__ == '__main__':
    print extract_correlation_()
    print extract_correlation()