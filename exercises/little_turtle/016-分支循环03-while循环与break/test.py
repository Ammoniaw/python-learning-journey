# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: test.py
# @Date: 2026/8/3
# @Description: 复读机

prompt = "请输入一句口号(输入STOP结束): "
while True:
    slogan = input(prompt)
    if slogan != "STOP":
        print(slogan, sep="")
    else:
        break
