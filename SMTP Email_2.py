#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:57:44 2018

@author: davidyang
"""
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr))

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP server:')
##16位授权码：qregdocdzzrobdic##

msg = MIMEMultipart()
msg['From'] = _format_addr('想你的胖远 <%s>' % from_addr)
msg['To'] = _format_addr('傻黎 <%s>' % to_addr)
msg['Subject'] = Header('星期天...', 'utf-8').encode()
#邮件正文是MIMEText
msg.attach(MIMEText('<html><body><h1>Lalalalalalalalalalala</h1>' +
    '<p>Share U an <a href="http://www.ttvdo.com/show/3145.html?Play=Ac_18">AV</a>...</p>' +
    '</body></html>', 'html', 'utf-8'))
#添加附件就是加上一个MIMEBase, 从本体读取一个图片：
with open('/Users/davidyang/Downloads/hci.docx', 'rb') as f:
    #设置附件的MIME和文件名
    mime = MIMEBase('text', 'docx', filename = 'hci.docx')
    #加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename = 'hci.docx')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    #把附件的内容读取进来：
    mime.set_payload(f.read())
    #用Base64编码：
    encoders.encode_base64(mime)
    #添加到MIMEMultipart:
    msg.attach(mime)


server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
