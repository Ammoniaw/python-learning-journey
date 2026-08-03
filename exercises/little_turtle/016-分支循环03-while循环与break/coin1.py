# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: coin1.py
# @Date: 2026/8/3
# @Description: 抛硬币
import random

counts = int(input("请输入抛硬币的次数："))
i = 0
# 利用变量来控制是否输出正反面信息
if counts > 100:
    ignore = True
else:
    ignore = False
# 正反面出现次数
purasu = 0
mainasu = 0
# 正反面连续最大次数
purasu_counts = 0
mainasu_counts = 0
# 正反面连续临时次数
j = 0
k = 0
print("开始抛硬币实验：")
while i < counts:
    num = random.randint(1, 10)
    if num % 2:
        purasu += 1
        if not ignore:  # counts>100次，ignore为True,不输出正反面
            print("正面", end=" ")
        # 每次出现正面 j加1 并且设置临时反面连续为0
        j += 1
        k = 0
        if j > purasu_counts:  # 如果j大于最大连续正面次数 就让最大连续次数统计+1 确保始终统计最大次数
            purasu_counts += 1

    else:
        mainasu += 1
        if not ignore:
            print("反面", end=" ")
        # 每次到反面 就设置正面连续变量j为0
        j = 0
        k += 1  # 每次到反面就 设置临时反面连续变量k+1
        if k > mainasu_counts:  # 确保始终统计最大次数
            mainasu_counts += 1
    i += 1

print(f"一共模拟了{counts}次抛硬币，结果如下：")
print(f"反面: {mainasu}次")
print(f"正面: {purasu}次")
print(f"最多连续正面:{purasu_counts}次")
print(f"最多连续反面:{mainasu_counts}次")
