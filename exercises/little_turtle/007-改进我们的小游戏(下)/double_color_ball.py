# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: double_color_ball.py
# @Date: 2026/8/2
# @Description: 模拟双色球
import random

red_balls = list(range(1, 34))
blue_balls = list(range(1, 16))
# sample() 从指定序列population中抽取k个不重复元素并返回
red_numbers = random.sample(population=red_balls, k=6)
blue_number = random.randint(1, 16)
print("开奖结果是:", *red_numbers)
print("特别号码是:", blue_number)
