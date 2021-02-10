# https://www.acmicpc.net/problem/11451

from collections import deque
import sys
input = sys.stdin.readline

def DFS(vertax):
	visited[vertax]=True
	next = adj[vertax]
	if not visited[next] :
		DFS(next)

for _ in range(int(input())):
	n = int(input())
	adj = [0]*(n+1) 
	visited = [False]*(n+1)
	cnt = 0

	for i, e in enumerate(list(map(int, input().split()))): # O(n)
		adj[i+1] = e
	
	for i in range(1,n+1):
		if not visited[i] :
			DFS(i)
			cnt += 1
	print(cnt)