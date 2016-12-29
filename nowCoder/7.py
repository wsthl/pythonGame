#-*- coding:utf-8 -*-
import sys
#对字符串字典进行排序
data = int(sys.stdin.readline())
list=[]
for i in range(data):
	list.append(str(sys.stdin.readline()))
list = sorted(list)
for i in list:
	print i[:len(i)-1]