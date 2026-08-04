# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: main_element.py
# @Date: 2026/8/4
# @Description: 查找列表的主要元素
target = [2, 2, 4, 2, 3, 6, 2]
# 对列表进行排序
target.sort()
print(target)
length = len(target)
middle_element = target[length // 2]
j = 0
for i in target:
    if i == middle_element:
        j += 1
        if j >= length // 2 + 1:
            print(f"主要元素为{i}")
            break
else:
    print("没有主要元素")
