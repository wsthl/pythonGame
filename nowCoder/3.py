#-*- coding=utf-8 -*-
import sys
#提取不重复数
while True:
	try:
		data = str(sys.stdin.readline())
		data = reversed(data)
		res = ""
		for i in data:
			if i not in res:
				res +=i 
		print int(res)
	except:
		break