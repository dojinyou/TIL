# https://www.acmicpc.net/problem/1476

import sys
input = sys.stdin.readline

def getYear(n):
	return ((n-1)%15+1,(n-1)%28+1,(n-1)%19+1)

e, s, m = map(int, input().split())
result = 1
while getYear(result) != (e,s,m) :
	result += 1
print(result)
