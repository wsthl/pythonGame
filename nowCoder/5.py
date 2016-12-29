#-*- coding:utf-8 -*-
import sys
#字符串翻转
data = str(sys.stdin.readline())
data = data[::-1]
res = ''
for i in range(1,len(data)):
	res+=data[i]
print res