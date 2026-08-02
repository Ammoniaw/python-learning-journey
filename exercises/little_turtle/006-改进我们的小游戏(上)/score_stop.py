# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: score_stop.py
# @Date: 2026/8/2
# @Description: 为score.py添加循环，与结束循环条件

while True:
    prompt = "请输入您的分数: "
    score = input(prompt)
    if score == 'e':
        break
    score = int(score)
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
