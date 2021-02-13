# https://www.acmicpc.net/problem/2146

from collections import deque
import sys
input = sys.stdin.readline

def makeIsland(i,j, num):
	q = deque([[i,j]])
	islands[i][j] = num
	while q :
		x, y = q.popleft()
		# print(f'makeIsland = {x}, {y}')
		if x > 0 and originMap[x-1][y] == 1 and islands[x-1][y] == 0:
			islands[x-1][y] = num
			q.append([x-1,y])
		if y > 0 and originMap[x][y-1] == 1 and islands[x][y-1] == 0:
			islands[x][y-1] = num
			q.append([x,y-1])
		if x < n-1 and originMap[x+1][y] == 1 and islands[x+1][y] == 0:
			islands[x+1][y] = num
			q.append([x+1,y])
		if y < n-1 and originMap[x][y+1] == 1 and islands[x][y+1] == 0:
			islands[x][y+1] = num
			q.append([x,y+1])
		


n = int(input())
originMap = []
islands = [[0]*n for _ in range(n)]
island_No = 1
for _ in range(n):
	originMap.append(list(map(int, input().split())))

q = deque()
for i in range(n):
	for j in range(n):
		if originMap[i][j] == 1:
			q.append([i,j])
			if islands[i][j] == 0:
				makeIsland(i,j, island_No)
				island_No += 1

print('------------------------')
for i in islands:
	print(i)
print('------------------------')

result = 200
prev = 0
while q :
	x,y = q.popleft()
	if result != 200 and prev != originMap[x][y] :
		print(result)
		break
	prev = originMap[x][y]
	if x > 0 :
		if islands[x-1][y] == 0 :
			islands[x-1][y] = islands[x][y]
			originMap[x-1][y] = originMap[x][y]+1
			q.append([x-1,y])
		elif islands[x-1][y] != islands[x][y]:
			result = min(result, originMap[x-1][y]+originMap[x][y]-2)
	if y > 0 :
		if islands[x][y-1] == 0 :
			islands[x][y-1] = islands[x][y]
			originMap[x][y-1] = originMap[x][y]+1
			q.append([x,y-1])
		elif islands[x][y-1] != islands[x][y] :
			result = min(result, originMap[x][y-1]+originMap[x][y]-2)
	if x < n-1 :
		if islands[x+1][y] == 0 :
			islands[x+1][y] = islands[x][y]
			originMap[x+1][y] = originMap[x][y]+1
			q.append([x+1,y])
		elif islands[x+1][y] != islands[x][y] :
			result = min(result, originMap[x+1][y]+originMap[x][y]-2)
	if y < n-1 :
		if islands[x][y+1] == 0 :
			islands[x][y+1] = islands[x][y]
			originMap[x][y+1] = originMap[x][y]+1
			q.append([x,y+1])
		elif islands[x][y+1] != islands[x][y] :
			result = min(result, originMap[x][y+1]+originMap[x][y]-2)

print('------------------------')
for i in originMap:
	print(i)
print('------------------------')
