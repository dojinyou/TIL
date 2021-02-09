# https://www.acmicpc.net/problem/1260

from collections import deque
def DFS(s):
	print(s, end=' ')
	visited[s] = True
	for e in adj[s]:
		if not visited[e] :
			DFS(e)

def BFS(s):
	q = deque([s])
	while q :
		v = q.popleft()
		if not visited[v] :
			print(v, end=' ')
			visited[v] = True
			for e in adj[v]:
				if not visited[e] :
					q.append(e)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
	x, y = map(int,input().split())
	adj[x].append(y)
	adj[y].append(x)

for l in adj:
	l.sort()

visited = [False]*(n+1)
DFS(v)
print()
visited = [False]*(n+1)
BFS(v)