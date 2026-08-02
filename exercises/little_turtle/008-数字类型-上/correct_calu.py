# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: correct_calu.py
# @Date: 2026/8/2
# @Description: 正确计算浮点数
import decimal

a = decimal.Decimal('0.1')
b = decimal.Decimal('0.3')
# 计算0.1 + 0.1 + 0.1 - 0.3
result = a + a + a - b
print(result)  # 0.0
