# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 15:27
# @Author  : Py.qi

import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite_env.settings'

if __name__ == '__main__':
    subject,from_email,to = u'来自我的测试邮件','920664709@163.com','920664709@qq.com'
    text_content = '欢迎访问www.baidu.com'
    html_content = '<p>欢迎访问<a href="http://www.baidu.com" target=blank>www.baidu.com</a>,这里是百度</p>'
    msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
    msg.attach_alternative(html_content,"text/html")
    msg.send()

