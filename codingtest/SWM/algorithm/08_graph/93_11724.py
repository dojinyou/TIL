# https://www.acmicpc.net/problem/11724

from collections import deque
import sys

def BFS(s):
	q = deque([s])
	while q :
		v = q.popleft()
		if not visited[v] :
			visited[v] = True
			for e in adj[v]:
				if not visited[e]:
					q.append(e)

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n+1)] # O(n)

for _ in range(m): # O(m)
	x, y = map(int,sys.stdin.readline().split())
	adj[x].append(y)
	adj[y].append(x)

cnt = 0 

visited = [False]*(n+1)
visited[0] = True
for i, isVisited in enumerate(visited): # O(n)
	if not isVisited :
		BFS(i)
		cnt += 1

print(cnt)