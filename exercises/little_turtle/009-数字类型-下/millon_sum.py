# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: millon_sum.py
# @Date: 2026/8/2
# @Description: 计算1000 000以内所有偶数的和
total = 0
for i in range(0, 1_000_001, 2):
    total += i
print(f"1000000以内所有偶数的和是: {total}")
