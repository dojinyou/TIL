# https://www.acmicpc.net/problem/9446

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def getCost(i):
	if len(made[i]) == 0 :
		return cost[i]
	minCost = cost[i]
	for x,y in made[i] :
		minCost = min(minCost, getCost(x)+getCost(y))
	return minCost

n, m = map(int, input().split())
cost = [0]
cost.extend(list(map(int, input().split())))
made = [[] for _ in range(n+1)]
for _ in range(m):
	a, x, y = map(int, input().split())
	made[a].append([x,y])
	
print(getCost(1))



