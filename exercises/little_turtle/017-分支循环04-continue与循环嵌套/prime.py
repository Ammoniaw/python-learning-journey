# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: prime.py
# @Date: 2026/8/3
# @Description:10 以内的所有素数
number = 1
while number < 10:
    number += 1
    if number == 2 or number == 3:
        print(f"{number}是一个素数。")
        continue
    j = 2
    while number % j == 0:
        print(f"{number} = {j} * {number // j}")
        j += 1
    else:
        print(f"{number}是一个素数。")
