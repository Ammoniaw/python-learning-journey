# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: count_words.py
# @Date: 2026/8/16
# @Description: 统计字符串中的单词个数
prompt = "请输入字符串:"
input_str = input(prompt)
# split返回列表 直接使用len()进行统计即可
count = len(input_str.split(' '))
print(f"输出: {count}")
