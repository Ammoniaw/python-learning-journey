# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: coin_toss_re.py
# @Date: 2026/8/2
# @Description:
# 导入随机模块 #
import random

# 接收用户输入并将数值赋值给 counts 变量 #
counts = int(input("请输入抛硬币的次数："))
i = 0

print("开始抛硬币实验：")
while i < counts:
    # 生成一个随机数num #
    num = random.randint(0, counts)
    if num % 2:
        # 打印结果 #
        print("正面", end=' ')
    else:
        # 打印结果 #
        print("反面", end=" ")

    i = i + 1
