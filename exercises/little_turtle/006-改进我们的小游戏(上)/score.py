# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: score.py
# @Date: 2026/8/2
# @Description: 成绩评级程序
prompt = "请输入您的分数: "
score = int(input(prompt))

if score == 100:
    print("S")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")