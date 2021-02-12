# https://www.acmicpc.net/problem/9466

from collections import deque
import sys
input = sys.stdin.readline

def makeTeam(i):
	teamMember = {i:0}
	nextMember = choice[i]
	visited[i] = True
	cnt = 1
	while nextMember not in teamMember :
		if visited[nextMember] :
			return cnt
		teamMember[nextMember] = cnt
		visited[nextMember] = True
		nextMember = choice[nextMember]
		cnt += 1
	return teamMember[nextMember]

for _ in range(int(input())):
	n = int(input())
	choice = [0]
	choice.extend(list(map(int,input().split())))
	visited = [False]*(n+1)
	cnt = 0
	for i in range(1,n+1):
		if not visited[i]:
			cnt += makeTeam(i)
	print(cnt)