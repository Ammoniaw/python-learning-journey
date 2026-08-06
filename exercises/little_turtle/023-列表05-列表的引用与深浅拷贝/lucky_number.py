# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: lucky_number.py
# @Date: 2026/8/6
# @Description: 找出矩阵中的幸运数字

matrix = [[10, 36, 52],
          [33, 24, 88],
          [66, 76, 99]]
min_list = []
for i in range(3):
    # 找出每个子列表中最小的数字 添加到列表中
    min_number = min(matrix[i])
    min_list.append(min_number)
# 找出最大的那个即是幸运数字
lucky_number = max(min_list)

print(lucky_number)
