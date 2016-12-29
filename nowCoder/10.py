L=[2,8,3,50]
res = 1
for i in L:
	res = res * i
	while res % 10 ==0:
		res = res /10

if res % 2 == 0:
	print 0
else:
	print 1

a =10 
s = bin(a)
count = 0
for i in range(2,len(s)):
	if s[i] == '1':
		count =count+1
	else:
		continue
print count