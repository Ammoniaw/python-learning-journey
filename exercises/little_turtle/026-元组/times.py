# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: times.py
# @Date: 2026/8/9
# @Description: 使用timeit模块
import timeit

# 测试创建列表的时间
test_list = timeit.repeat('x = ["123"]', repeat=100)
# 测试创建元组的时间
test_tuple = timeit.repeat('x = ("123")', repeat=100)

result_list = sum(test_list) / 100
result_tuple = sum(test_tuple) / 100
print(f"{result_list=}, {result_tuple=}")

# result_list=0.04046112099953461, result_tuple=0.020012311001773923,似乎是元组更快
