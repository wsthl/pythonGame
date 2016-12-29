#-*- coding:utf-8 -*-
import sys

def count_num(num):
	count = 0 
	b = []
	for a in num:
		if a not in b:
			b.append(a)

	for c in b:
		if(ord(c) >=0 and ord(c) <= 127):
			count+=1

	return count

s = str(sys.stdin.readline())
print count_num(s)
