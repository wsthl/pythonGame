#-*- coding:utf-8 -*-
import sys
#购物单
N = int(sys.stdin.readline()) #总钱数
m = int(sys.stdin.readline()) #希望购买物品数

v=[] #表示该物品的价格
p=[] #表示该物品的重要度
q=[] #表示该物品是主件，还是附件，其中=0为主，>0为附件

for i in range(m):
	v.append()