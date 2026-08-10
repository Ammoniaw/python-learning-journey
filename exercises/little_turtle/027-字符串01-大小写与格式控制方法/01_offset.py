# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Author: Ammoniaw
# @FileName: 01_offset.py
# @Date: 2026/8/9
# @Description: 偏移字母

s = "x7y8z9"
new_s = ''
for i in range(len(s)):
    if i % 2 == 0:
        new_s += s[i]
    else:
        if ord(s[i - 1]) + int(s[i]) > ord('z'):
            new_s += chr(ord(s[i - 1]) + int(s[i]) - ord('z') + ord('a') - 1)
        else:
            new_s += chr(ord(s[i - 1]) + int(s[i]))

print(new_s)
