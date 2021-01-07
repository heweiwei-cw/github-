# -*- coding:utf-8 -*-
# @Time : 2020/11/21 22:38
# @Author : Double Wei
# @File : encode_exercise.py
# @Software : PyChar
import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
html = response.read().decode("utf-8")
print(html)