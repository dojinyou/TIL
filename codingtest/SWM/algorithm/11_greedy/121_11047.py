# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
values = [int(input()) for _ in range(n)]

count = 0
for i in range(1,n+1):
	value = values[n-i]
	if value > k :
		continue
	count += k//value
	k = k%value
	if k == 0 :
		print(count)
		break
