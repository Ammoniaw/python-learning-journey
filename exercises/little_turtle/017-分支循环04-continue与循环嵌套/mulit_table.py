# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: mulit_table.py
# @Date: 2026/8/3
# @Description: 倒着的乘法表
k = 1
while True:
    j = 9
    while k <= j:
        print(f"{j} * {k} = {j * k}", end="\t")
        j -= 1
    k += 1
    if k > 9:
        break
    print("")
