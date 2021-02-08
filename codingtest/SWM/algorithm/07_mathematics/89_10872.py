# https://www.acmicpc.net/problem/10872

from functools import reduce
n = int(input())
if n == 0 :
	print(1)
else :
	print(reduce(lambda x,y : x*y, range(1,n+1)))

