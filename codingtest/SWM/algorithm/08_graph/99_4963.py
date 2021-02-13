# https://www.acmicpc.net/problem/4963

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def checkIsland(i,j):
	if houseMap[i][j] != 0 :
		houseMap[i][j] = 0
		checkIsland(i+1,j)
		checkIsland(i,j+1)
		checkIsland(i+1,j+1)
		checkIsland(i+1,j-1)
		checkIsland(i-1,j)
		checkIsland(i,j-1)
		checkIsland(i-1,j-1)
		checkIsland(i-1,j+1)

while True :
	w, h = map(int, input().split())
	if w == 0 and h == 0 :
		break
	if w == 0 or h == 0 :
		print(0)
		continue
	houseMap = [[0]*(w+2)]
	for i in range(1,h+1):
		houseMap.append([0])
		houseMap[i].extend(list(map(int, input().split())))
		houseMap[i].append(0)
	houseMap.append([0]*(w+2))
	cnt = 0
	for i in range(1,h+1):
		for j in range(1,w+1):
			if houseMap[i][j] != 0 :
				checkIsland(i,j)
				cnt += 1
	print(cnt)

