#! /usr/bin/env python
# coding:utf-8
__author__ = 'Farley'

import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib,os


# 测试图片上传
#
# url = 'http://weedfs.che-mi.net/weedfs-fileupload/rest/file/fileupload.do'
# file = {
#     'newfile':open('C:/Users/Public/Pictures/Sample Pictures/1447007795_9803.jpg','rb')
# }
#
#
# r = requests.post(url,files=file)
# print r.text


def send_mail(file_new):
    msg = MIMEMultipart()

    # 正文部分
    part = MIMEText("各位好:\n   接口测试报告见附件,请查收,谢谢!")
    msg.attach(part)

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
        smtp.login("44248556@qq.com", "gilrncumgsubcbee")

        # 发送多个人时用列表形式,["xxx@qq.com","aaa@qq.com"]
        smtp.sendmail("44248556@qq.com","2881510217@qq.com",msg=msg.as_string())
        smtp.quit()
    except Exception as e:
        print e

def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda f:os.path.getmtime(test_report  + f),reverse=False)
    file_new = os.path.join(test_report,lists[-1])
    return file_new

if __name__ == '__main__':
    test_report = 'E:/Pyscript/fangche/Report/'     # 测试报告存放路径
    new_report = new_report(test_report)
    send_mail(new_report)


