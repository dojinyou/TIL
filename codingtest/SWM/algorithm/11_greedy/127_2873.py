# https://www.acmicpc.net/problem/2873

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
happyPoints = [list(map(int,input().split())) for _ in range(h)]
result = ''

if h % 2 == 1 :
	result += 'R'*(w-1)+'D'
	for i in range(h//2):
		result += 'L'*(w-1)+'D'+'R'*(w-1)+'D'
	print(result[:-1])
elif w % 2 == 1 :
	result += 'D'*(h-1)+'R'
	for i in range(w//2):
		result += 'U'*(w-1)+'R'+'D'*(w-1)+'R'
	print(result[:-1])
else : # 패턴 확인 필요
	minValue = happyPoints[0][1]
	minPoint = [0,1]
	for i in range(h):
		for j in range(w//2):
			value = happyPoints[i][2*j+(i+1)%2]
			if value < minValue :
				minValue = value
				minPoint[0] = i
				minPoint[1] = 2*j+(i+1)%2
	if minPoint[1] % 2 == 0 :
		for i in range(minPoint[1]//2):
			result += 'D'*(h-1)+'R'+'U'*(h-1)+'R'
		pattern = 'RDLD'
		for i in range(h//2):
			if minPoint[0]//2-1 == i :
				result += 'RDD'
				pattern = 'LDRD'
			result += pattern
		result = result[:-1]
		result += 'D'
		for i in range(minPoint[1]//2):
			result += 'D'*(h-1)+'R'+'U'*(h-1)+'R'
