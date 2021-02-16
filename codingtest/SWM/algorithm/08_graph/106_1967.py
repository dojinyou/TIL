# https://www.acmicpc.net/problem/1967

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def DFS(index, result, root):
	for i, w in adj[index]:
		if i == root :
			continue
		if result[i] == 0 :
			result[i] = result[index]+w
			DFS(i, result, root)

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
	p, c, w = map(int,input().split())
	adj[p].append((c,w))
	adj[c].append((p,w))

res = [0 for _ in range(n+1)]
DFS(1,res, 1)

mv = 0
mi = 0
for i,v in enumerate(res):
	if mv < v :
		mv = v
		mi = i
res = [0 for _ in range(n+1)]
DFS(mi, res, mi)
print(max(res))