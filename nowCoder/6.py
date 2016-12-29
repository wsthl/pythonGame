#-*- coding:utf-8 -*-
import sys
#句子逆序
data = str(sys.stdin.readline())
res = data.split(' ')
res = res[::-1]
s = res[0][:len(res[0])-1]
for i in range(1,len(res)):
	s +=" "
	s +=res[i]
print s