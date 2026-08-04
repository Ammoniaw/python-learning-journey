# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: input_target.py
# @Date: 2026/8/4
# @Description: 输入列表与目标 获取索引


list_prompt = "请输入一个整数（输入STOP结束）："
target_prompt = "请输入目标整数："
list1 = []
while True:
    # 请求用户输入列表
    element = input(list_prompt)

    if element == 'STOP':
        break
    else:
        list1.append(int(element))
target = int(input(target_prompt))
# target = 100
# list1 = [22, 33, 45, 18, 62, 88, 93, 72, 67, 19]
# 给出结果
for i in range(len(list1) - 1):
    for j in range(i, len(list1) - 1):
        if list1[i] + list1[j + 1] == target:
            print([i, j + 1])
            break
