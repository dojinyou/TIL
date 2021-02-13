# https://www.acmicpc.net/problem/2178

from collections import deque
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
searchMap = [[] for _ in range(h)]
q = deque()
for i in range(h):
	for c in input().rstrip() :
		searchMap[i].append(int(c))

q.append([1,0,0])
while q :
	v, x, y = q.popleft()
	if x > 0 and searchMap[x-1][y] == 1 :
		searchMap[x-1][y] = v+1
		q.append([v+1, x-1, y])
	if x < h-1 and searchMap[x+1][y] == 1 :
		searchMap[x+1][y] = v+1
		q.append([v+1, x+1, y])
	if y > 0 and searchMap[x][y-1] == 1 :
		searchMap[x][y-1] = v+1
		q.append([v+1, x, y-1])
	if y < w-1 and searchMap[x][y+1] == 1 :
		searchMap[x][y+1] = v+1
		q.append([v+1, x, y+1])

print(searchMap[-1][-1])