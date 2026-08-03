# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: coin.py
# @Date: 2026/8/3
# @Description: 抛硬币
import random

counts = int(input("请输入抛硬币的次数："))
i = 0
purasi = 0
manasi = 0
print("开始抛硬币实验：")
if counts < 100:
    while i < counts:
        num = random.randint(1, 10)
        if num % 2:
            purasi += 1
            print("正面", end=" ")
        else:
            manasi += 1
            print("反面", end=" ")

        i += 1
else:
    while i < counts:
        num = random.randint(1, 10)
        if num % 2:
            purasi += 1
        else:
            manasi += 1

        i += 1

print(f"一共模拟了{counts}次抛硬币，结果如下：")
print(f"反面: {manasi}次")
print(f"正面: {purasi}次")
