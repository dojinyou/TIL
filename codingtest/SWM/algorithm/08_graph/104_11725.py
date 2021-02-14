# https://www.acmicpc.net/problem/11725

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
parents = [0]*(n+1)
parents[0], parents[1] = 1, 1
childs = [[] for _ in range(n+1)]
q = deque()

for _ in range(n-1):
	v1, v2 = map(int, input().split())
	if parents[v1]:
		parents[v2] = v1
		childs[v1].append(v2)
	elif parents[v2]:
		parents[v1] = v2
		childs[v2].append(v1)
	else :
		childs[v1].append(v2)
		childs[v2].append(v1)
for i in childs[1]:
	q.append(i)
while q :
	p = q.popleft()
	print(f'q value = {p}, p child = {childs[p]}')
	for i in childs[p]:
		if i != parents[p]:
			parents[i] = p
			q.append(i)
for i in parents[2:]:
	print(i)