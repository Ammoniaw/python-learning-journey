# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: alcohol.py
# @Date: 2026/8/3
# @Description: 判断是否构成饮酒行为
prompt = "请输入酒精含量："
alcohol = int(input(prompt))

if alcohol <= 20:
    print("不构成饮酒行为")
elif alcohol <= 80:
    print("已经达到酒后驾驶的标准")
else:
    print("已经达到醉酒驾驶的标准")
