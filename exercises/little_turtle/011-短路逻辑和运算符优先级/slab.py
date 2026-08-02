# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: slab.py
# @Date: 2026/8/2
# @Description: 爱因斯坦的数学问题

steps = 7
i = 1
flag = False

while i < 10000:
    if (i % 2 == 1) and (i % 3 == 2) \
            and (i % 5 == 4) and (i % 6 == 5) \
            and (i % 7 == 0):
        flag = True
        break
    else:
        steps = i + 1
    i = i + 1

if flag:
    print('阶梯数是：', steps)
else:
    print('在程序限定的范围内找不到答案！')
