# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: matrix.py
# @Date: 2026/8/6
# @Description: 生成随机数矩阵列表 找出指定数
import random

target_number = int(input("请输入一个待匹配的整数："))

matrix_list = []
for i in range(1, 89):
    list1 = []
    for j in range(1, 89):
        # 要求1 随机整数取值范围 0-1024
        number = random.randint(0, 1024)
        if target_number == number:
            # 要求2 找出所有匹配元素 并输出行、列号
            print(i, j)
        list1.append(number)
    matrix_list.append(list1)
# print(matrix_list)
