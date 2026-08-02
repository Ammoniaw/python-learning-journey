# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: leap_year.py
# @Date: 2026/8/2
# @Description: 判断年份是否为闰年

# 请求用户输入一个年份
year = int(input("请输入一个年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}是闰年！")
else:
    print(f"{year}不是闰年！")
