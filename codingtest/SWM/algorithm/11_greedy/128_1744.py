# https://www.acmicpc.net/problem/1744

import sys
input = sys.stdin.readline

n = int(input())
visited = [False]*n
numList = []
result = 0
cnt = [0,0,0] # 음수, 0 또는 1의 개수

for i in range(n):
	num = int(input())
	numList.append(num)
	if num < 0 :
		cnt[0] += 1
	elif num == 0:
		cnt[1] += 1
	elif num == 1:
		cnt[2] += 1

numList.sort()

# 음수처리
if cnt[0] % 2 == 1 : # 홀수일 경우
	if cnt[1] > 0 : #0이 1개 이상일 경우
		cnt[0] += 1
		cnt[1] -= 1
	else :
		result += numList[cnt[0]-1]
		visited[cnt[0]-1] = True

for i in range(cnt[0]//2):
	result += numList[2*i]*numList[2*i+1]
	visited[2*i] = True
	visited[2*i+1] = True
print(f'음수 처리 {result}')


# 0과1 처리
for i in range(cnt[1]+cnt[2]): 
	result += numList[cnt[0]+i]
	visited[cnt[0]+i] = True
print(f'0과 1처리 {result}')

# 양수처리

for i in range(n-sum(cnt)):
	if visited[n-1-i]:
		continue
	if visited[n-2-i]:
		result += numList[n-1-i]
		visited[n-1-i] = True
	else :
		result += numList[n-1-i]*numList[n-2-i]
		visited[n-1-i] = True
		visited[n-2-i] = True

# print(f'양수처리 {result}')
print(result)