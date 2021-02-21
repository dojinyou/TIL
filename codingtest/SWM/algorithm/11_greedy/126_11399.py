# https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

n = int(input())
timeList = list(map(int,input().split()))
timeList.sort()

result = 0
for i, t in enumerate(timeList):
	result += t*(n-i)
print(result)