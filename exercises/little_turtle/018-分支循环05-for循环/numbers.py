# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: numbers.py
# @Date: 2026/8/3
# @Description: 输出1000以内的水仙花数


for num in range(2, 1000):
    g = num % 10
    s = num // 10 % 10
    b = num // 100
    number = pow(g, 3) + pow(s, 3) + pow(b, 3)
    if num == number:
        print(f"{num}")
