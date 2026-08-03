# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: numbers.py
# @Date: 2026/8/3
# @Description: 判断数字
prompt = "请输入一个数字："
num = int(input(prompt))

if num % 2 == 0:
    print(f"{num}是一个偶数。")
else:
    print(f"{num}是一个奇数。")
