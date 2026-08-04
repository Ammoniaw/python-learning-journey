# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: target_index.py
# @Date: 2026/8/4
# @Description: 输出达成目标的列表索引
list1 = [2, 7, 11, 15]
j = 0
target = 9
length = len(list1)
while True:
    for i in range(j, length - 1):
        if list1[i] + list1[i + 1] == target:
            print([i, i + 1])
    j += 1
    if j == length - 1:
        break
