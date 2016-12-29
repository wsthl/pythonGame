#-*- coding:utf-8 -*-
#取近视值
import sys
while True:
	try:
		data = float(sys.stdin.readline())
		print int(round(data))
	except:
		break