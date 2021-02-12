# https://www.acmicpc.net/problem/2667

import sys
input = sys.stdin.readline

def checkHouse(i,j):
	if houseMap[i][j] == 0 :
		return 0
	houseMap[i][j] = 0
	return 1 + checkHouse(i+1,j)+checkHouse(i,j+1)+checkHouse(i-1,j)+checkHouse(i,j-1)

n = int(input())
houseMap = [[0]*(n+2)]
for i in range(1,n+1):
	houseMap.append([0])
	for c in input() :
		houseMap[i].append(int(c) if c != '\n' else 0)
houseMap.append([0]*(n+2))
result = []
for i in range(1,n+1):
	for j in range(1,n+1):
		if houseMap[i][j] != 0 :
			cnt = checkHouse(i,j)
			if cnt != 0 :
				result.append(cnt)
print(len(result))
for i in sorted(result) :
	print(i)

