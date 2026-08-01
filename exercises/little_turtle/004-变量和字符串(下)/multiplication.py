# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: multiplication.py
# @Date: 2026/8/1
# @Description: 创建99乘法表
for i in range(1, 10):  # 控制行数
    for j in range(1, i+1):  # 控制列数
        print(f'{i} * {j} = {i*j}', end='\t')  # 使用f-string输出，并使用end控制输出格式
    print('')
