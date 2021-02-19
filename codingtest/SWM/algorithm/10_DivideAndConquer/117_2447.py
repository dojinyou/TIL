# https://www.acmicpc.net/problem/2447

import sys
input = sys.stdin.readline

n = int(input())
starMap = [['*']*n for _ in range(n)]
def star(n,x,y):
	if n == 3:
		starMap[x+1][y+1] = ' '
	else :
		miniN = n//3
		for i in range(3):
			for j in range(3):
				if i == 1 and j == 1:
					for k in range(miniN):
						for l in range(miniN):
							starMap[x+i*miniN+k][y+j*miniN+l] = ' '
				else :
					star(miniN, x+i*miniN,y+j*miniN)

star(n,0,0)
for row in starMap:
	print(''.join(row))
