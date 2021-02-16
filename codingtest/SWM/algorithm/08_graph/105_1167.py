# https://www.acmicpc.net/problem/1167

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def DFS(index, result):
	for i, d in distance[index]:
		if result[i] == 0 :
			result[i] = result[index]+d
			DFS(i, result)

n = int(input())
distance = [0]*(n+1)
for _ in range(n):
	inputList = list(map(int,input().split()))
	distance[inputList[0]] = [(inputList[i], inputList[i+1]) for i in range(1,len(inputList)-1,2)]

res = [0 for _ in range(n+1)]
DFS(1,res)
res[1] = 0

mv = 0
mi = 0
for i,v in enumerate(res):
	if mv < v :
		mv = v
		mi = i
res = [0 for _ in range(n+1)]
DFS(mi, res)
res[mi] = 0
print(max(res))



# 최대값을 오버해서 찾음
# def getIndex() :
# 	mValue = 0
# 	index = 0
# 	for i in range(1,n+1):
# 		if d[i] > mValue and not v[i] :
# 			mValue = d[i]
# 			index = i
# 	return index

# def dijkstra(s):
# 	print(f'dijkstra {s}')
# 	for i in range(1, n+1):
# 		d[i] = adj[s][i]
# 		v[i] = False
	
# 	v[s] = True
# 	for _ in range(n-2):
# 		cur = getIndex()
# 		v[cur] = True
# 		for j in range(1, n+1):
# 			if not v[j] :
# 				if d[cur] + adj[cur][j] > d[j] :
# 					print(f'direction {s}->{cur}->{j} d_new = {d[cur]+adj[cur][j]}, d_old = {d[j]}')
# 					d[j] = d[cur] + adj[cur][j]

# n = int(input())
# adj = [[0]*(n+1) for _ in range(n+1)]

# v = [False] * (n+1)
# d = [0] * (n+1)

# for _ in range(n):
# 	inputList = list(map(int,input().split()))
# 	for i in range(1,len(inputList)-1,2) :
# 		adj[inputList[0]][inputList[i]] = inputList[i+1]

# result = 0
# for i in range(1,n+1):
# 	dijkstra(i)
# 	for j in d :
# 		print(j, end='-')
# 	print('\n-----------------------')
# print(result)



# 시간초과
# def DFS(index, checkList):
# 	# print(f'DFS i = {index}, distance = {distance}, checkList = {checkList}')
# 	maxValue = 0
# 	for i, d in distance[index]:
# 		if i not in checkList:
# 			maxValue = max(maxValue, d + DFS(i, checkList | {i}))
# 	return maxValue

# n = int(input())
# distance = [0]*(n+1)
# for _ in range(n):
# 	inputList = list(map(int,input().split()))
# 	distance[inputList[0]] = [(inputList[i], inputList[i+1]) for i in range(1,len(inputList)-1,2)]
# # print(distance)
# result = 0
# for i in range(1,n+1):
# 	result = max(result, DFS(i, {i}))
# print(result)




# 메모리 초과 실패
# n = int(input())
# distance = [[0]*(n+1) for _ in range(n+1)]
# result = 0
# for i in range(1,n+1):
# 	d = list(map(int,input().split()))
# 	for j in range(1,len(d),2):
# 		if d[j] == -1 :
# 			break
# 		distance[i][d[j]] = d[j+1]
# # for d in distance:
# # 	print(d)
# # print('-----------------------')
# for i in range(1,n+1):
# 	# print(i)
# 	for j, d in enumerate(distance[i]):
# 		if d != 0 :
# 			for k, _d in enumerate(distance[j]):
# 				if k != i and _d != 0    :
# 					distance[i][k] = min(distance[i][k],d+_d) if distance[i][k] != 0 else d+_d

# # [print(d) for d in distance]
# for i in range(1,n+1):
# 	for j in range(i+1,n+1):
# 		result = max(result, distance[i][j])

# print(result)
