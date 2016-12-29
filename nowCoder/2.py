#-*- coding:utf-8 -*-

#合并表记录
import sys

while True:
	try:
		dic = {}
		n = int(sys.stdin.readline())
		for i in range(n):
			content = str(sys.stdin.readline())
			key = content.split(" ")[0]
		 	key = int(key)
		 	value = content.split(" ")[1]
		 	if key in dic:
		 		dic[key]=dic[key]+int(value)
		 	else:
		 		dic[key]=int(value)
		dic = sorted(dic.items(),key=lambda d:d[0])
		for d in dic:
			print d[0],d[1]
	except:
		break



