#! /usr/bin/env python
# coding:utf-8

__author__ = 'Farley'

import unittest
import time
import HTMLTestRunner
from model.log import logger
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib,os

# python2.* 加下面两句,防止乱码
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def suite():
    dir_case = unittest.defaultTestLoader.discover(
               start_dir='E:/Pyscript/fangche/test_case/',
               pattern='test_*.py',
               top_level_dir=None
    )
    return dir_case

def getNowTime():
    return time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

def runAuto():
    logger.info('开始执行测试脚本...')
    filename = 'E:/Pyscript/fangche/Report/' + getNowTime() + 'TestReport.html'
    fp = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
             stream=fp,
             title=u'接口自动化测试报告',
             description=u'自动化测试报告详细信息'
             )
    runner.run(suite())

def send_mail(file_new):
    msg = MIMEMultipart()

    # 正文部分
    body = MIMEText("各位好:\n   接口测试报告已发送,详情请下载附件查看,谢谢!")
    msg.attach(body)

    # 构造附件
    att1 = MIMEText(open(file_new,'rb').read(),'base64','utf-8')
    att1['Conten-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment;filename="接口测试报告.html"'    #filename要带格式(如htm,txt等)
    msg.attach(att1)

    # 构造附件2
    # ......

    msg['to'] = '2881510217@qq.com'
    msg['from'] = '44248556@qq.com'
    msg['Subject'] = u"接口自动化测试报告"

    try:
        smtp = smtplib.SMTP_SSL()
        smtp.connect('smtp.qq.com')
        smtp.login("44248556@qq.com", "password,或者客户端授权码")

        # 发送给多个人时用列表形式,["xxx@qq.com","aaa@qq.com"]
        smtp.sendmail("44248556@qq.com","2881510217@qq.com",msg=msg.as_string())
        smtp.quit()
    except Exception as e:
        print e

def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda f:os.path.getmtime(test_report + f),reverse=False)
    file_new = os.path.join(test_report,lists[-1])
    return file_new

if __name__ == '__main__':
    runAuto()
    test_report = 'E:/Pyscript/fangche/Report/'     # 测试报告存放路径
    new_report = new_report(test_report)
    send_mail(new_report)
