# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

def getCount(length):
	s = 0
	for line in lines:
		s += line//length
	return s

k, n = map(int, input().split())
lines =[int(input()) for _ in range(k)]

s = 0
e = max(lines)
result = 0
while s+1 < e :
	t = (s+e)//2
	if getCount(t) >= n :
		result = t
		s = t
	else :
		e = t

result = e if getCount(e) >= n else result
print(result)
