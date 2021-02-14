# https://www.acmicpc.net/problem/1167

import sys
input = sys.stdin.readline

n = int(input())
distance = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
	d = list(map(int,input().split()))
	l = len(d)
	for j in range(1,l,2):
		if d[j] == -1 :
			break
		distance[i][d[j]] = d[j+1]
print(distance)