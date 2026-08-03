# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: number2.py
# @Date: 2026/8/3
# @Description: 回文数
prompt = "请输入一个整数: "
number = int(input(prompt))

# 判断该数字是否为回文数
if number < 0:
    print(f"{number}不是一个回文数")
elif number < 10:
    print(f"{number}是一个回文数")
else:
    num = number
    result = 0
    while True:
        if number >= 10:
            g = number % 10
            number //= 10
            result = result * 10 + g
        else:
            break
    result = result * 10 + number
    if num == result:
        print(f"{num}是一个回文数")
    else:
        print(f"{num}不是一个回文数")

"""
组合出一个回文数 回文数逆转之后与之前的数字相等
number = 12321
result = 0
while True:
    if number >= 10:
        g = number % 10
        print(g)
        number //= 10
        result = result * 10 + g
    else:
        print(number)
        break
result = result * 10 + number
print(result)
"""
