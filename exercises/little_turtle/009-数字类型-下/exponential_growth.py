# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: exponential_growth.py
# @Date: 2026/8/2
# @Description: 指数增长
import math

total = 0
for i in range(0, 64):
    total += math.pow(2, i)
print(f"舍罕王应该给达依尔 {total}粒麦子！")
# 没有显示完整数字的原因在于pow的结果超出2^53，且大数字默认科学计数法

# 第二种方法
total = 0
for i in range(0, 64):
    total += 2 ** i
print(f"舍罕王应该给达依尔 {total}粒麦子！")  # 舍罕王应该给达依尔 18446744073709551615粒麦子！
# python的整数是任意精度的，可以原样显示所有位数
