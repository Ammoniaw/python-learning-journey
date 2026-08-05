# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: nested_list.py
# @Date: 2026/8/5
# @Description: 创建嵌套列表

# 列表x 直接赋值
list_x = [0, 0, 0]

# 列表y - 二维列表
list_y = [0, 0, 0]
for j in range(3):
    list_y[j] = [0] * 3

# 列表z - 三维列表
list_z = [0, 0, 0]
for j in range(3):
    list_z[j] = [0] * 3
    for k in range(3):
        list_z[j][k] = [0] * 2

print(f"{list_x=}")
print(f"{list_y=}")
print(f"{list_z=}")
"""
list_x=[0, 0, 0]
list_y=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
list_z=[[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]
"""
