#-*-coding:utf-8 -*-
import sys
#求int型整数在内存中存储
data = int(sys.stdin.readline())
res =  bin(data)
count = 0
for i in range(2,len(res)):
	if res[i] == '1':
		count+=1
print count
