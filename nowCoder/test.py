'''
a={1:1,2:2,3:3}


list = a.keys()
for i in range(len(list)-1):
	print list[i],
	print ',',
print list[-1]

res = str(list[0])
for i in range(1,len(list)):
	res=res+","+str(list[i])
print res


print ','.join(map(str,a.keys()))
'''
'''
a = '123456'
res = ''
for i in range(0,len(a),2):
	res+=str(a[i])
print res
'''
'''
def prime(n):
	if n==1:
		return False
	for i in range(2,n/2+1):
		if n%i==0:
			return False
		return True

print ' '.join([str(i) for i in filter(prime,range(1,100))])
'''
'''
L=[0,1,2,3,4]
L.sort()
if len(L)%2 == 0:
	m = len[L]/2
	mid=L[m]+L[m-1]
	if mid %2 == 0:
		print mid/2
	else:
		print mid/2.0
else:
	mid = L[int(len(L)+1)/2-1]
	print mid

'''

'''
L=[2,8,3,50]

def count(L):
	num = 0
	res = 1
	for i in L:
		res = res * i
		while res % 10 ==0 :
			res = res/10
			num=num+1
	return num 
print count(L) 

def judge(L):
	num = 0 
	res = 1
	for i in L:
		res 
'''
'''
a = 24
b = 16

def gcd(a,b):
	if a < b:
		return gcd(b,a)
	elif b == 0:
		return a
	else :
		return gcd(b,a%b)
print gcd(a,b)

n = gcd(a,b)
coun/t =0
for i in range(1,n+1):
	if (n%i == 0):
		count= count+1

print count
'''
'''
a = 'a'
print ord('')
print chr(98)
'''
def tranfer(a,b):
	n = ord(a)
	n = n + 3
	if n > 122:
		n = n % 122
		n = n + 96
	return chr(n)
a = 'cagy'
b = 3
res = ''
for i in a :
	print i
	res = res + tranfer(i,b)

print res

print ord('a')
print ord('z')
