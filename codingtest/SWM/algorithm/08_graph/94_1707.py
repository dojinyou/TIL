# https://www.acmicpc.net/problem/1707

from collections import deque
import sys
input = sys.stdin.readline
def checkBG(vertax):
	q = deque([vertax])
	color[vertax] = 1
	while q :
		v = q.popleft()
		print(f'v={v}')
		for i in adj[v]:
			if color[i] == 0:
				q.append(i)
				color[i] = -color[v]
			elif color[v] == color[i] :
				return False
	return True

for _ in range(int(input())):
	v, e = map(int, input().split())
	adj = [[] for _ in range(v+1)] # O(n)
	
	for _ in range(e): # O(m)
		x, y = map(int,input().split())
		adj[x].append(y)
		adj[y].append(x)

	color = [0]*(v+1)
	isBinary = True
	for i in range(1, v+1):
		if color[i] == 0 :
			if not checkBG(i) :
				isBinary = False
				break
	print('Yes' if isBinary else 'No')

# def DFS(vertax):
# 	q = deque([vertax])
# 	while q :
# 		v = q.popleft()
# 		if not visited[v] :
# 			visited[v] = True
# 			if not color[v] :
# 				color[v] = 1
# 			else :
# 				color[v] *= -1
# 			for i in adj[v]:
# 				if not visited[i] :
# 					q.append(i)
# 					color[i] = color[v]

# for _ in range(int(sys.stdin.readline())):
# 	n, m = map(int, sys.stdin.readline().split())

# 	visited = [False for _ in range(n+1)]
# 	color = [0 for _ in range(n+1)]
# 	adj = [[] for _ in range(n+1)]

# 	for _ in range(m):
# 		x, y = map(int, sys.stdin.readline().split())
# 		adj[x].append(y)
# 		adj[y].append(x)
	
# 	for i in range(1, n+1):
# 		if not visited[i]:
# 			DFS(i)
	
# 	isBinary = True
# 	for i in range(1,n+1):
# 		for j in adj[i]:
# 			if color[i] == color[j]:
# 				isBinary = False
# 				break
# 		if not isBinary :
# 			print('No')
# 			break
# 	if isBinary :
# 		print('Yes')

