# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())
timeList = [tuple(map(int,input().split())) for _ in range(n)]
sortedTimeList = sorted(timeList, key=lambda x:(x[1],x[0]))

count = 0
endTime = 0
for s,e in sortedTimeList:
	if endTime <= s :
		endTime = e
		count += 1
print(count)