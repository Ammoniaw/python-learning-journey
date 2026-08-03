# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: jiaogu.py
# @Date: 2026/8/3
# @Description: 验证角谷猜想
n = int(input("请输入一个正整数："))

while n > 0:
    if n % 2 == 0:
        print(f"{n}/2 = {int(n / 2)}")
        n = int(n / 2)
    else:
        print(f"{n}*3+1 = {int(n * 3 + 1)}")
        n = int(n * 3 + 1)
    if n == 1:
        break
