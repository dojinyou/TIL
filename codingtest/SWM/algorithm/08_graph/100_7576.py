# https://www.acmicpc.net/problem/7576

from collections import deque
import sys
input = sys.stdin.readline

w, h = map(int, input().split())
box = [[] for _ in range(h)]
q = deque()
cnt = 0
result = -1

for i in range(h):
	for j, t in enumerate(input().split()):
		box[i].append(int(t))
		if t == "1":
			q.append([1,i,j])
		if t == "-1":
			cnt += 1

while q :
	v, x, y = q.popleft()
	cnt += 1
	result = max(result, v)
	if x > 0 and box[x-1][y] == 0 :
		box[x-1][y] = v+1
		q.append([v+1,x-1,y])
	if x < h-1 and box[x+1][y] == 0 :
		box[x+1][y] = v+1
		q.append([v+1,x+1,y])
	if y > 0 and box[x][y-1] == 0 :
		box[x][y-1] = v+1
		q.append([v+1,x,y-1])
	if y < w-1 and box[x][y+1] == 0 :
		box[x][y+1] = v+1
		q.append([v+1,x,y+1])

if cnt < w*h :
	print(-1)
else :
	print(result-1)