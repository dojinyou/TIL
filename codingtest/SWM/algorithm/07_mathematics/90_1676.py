# https://www.acmicpc.net/problem/1676

from functools import reduce
n = int(input())
if n < 4 :
	print(0)
else :
	result = str(reduce(lambda x,y : x*y, range(1,n+1)))[::-1]
	cnt = 0
	for i in result:
		if i == '0' :
			cnt +=1
		else :
			print(cnt)
			break
