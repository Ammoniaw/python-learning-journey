# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: bonus.py
# @Date: 2026/8/3
# @Description: 奖金
prompt = "请输入今年的利润: "
profit = int(input(prompt))
bonus = 0
if profit <= 100_000:
    bonus = profit * 0.1
elif profit <= 200_000:
    bonus = 100_0000 * 0.1 + (200_0000 - profit) * 0.075
elif profit <= 400_000:
    bonus = 100_000 * 0.1 + 100_0000 * 0.075 + \
            (400_000 - profit) * 0.05
elif profit <= 600_000:
    bonus = 100_000 * 0.1 + 100_000 * 0.075 + \
            200_000 * 0.05 + (profit - 600_000) * 0.03
elif profit <= 1_000_000:
    bonus = 100_000 * 0.1 + 100_000 * 0.075 + \
            200_000 * 0.05 + 200_000 * 0.03 + \
            (profit - 600_000) * 0.015
elif profit > 1_000_000:
    bonus = 100_000 * 0.1 + 100_000 * 0.075 + \
            200_000 * 0.05 + 200_000 * 0.03 + \
            400_000 * 0.015 + (profit - 1_000_000) * 0.01
print(f"应该发放的奖金总数是: {bonus}")
