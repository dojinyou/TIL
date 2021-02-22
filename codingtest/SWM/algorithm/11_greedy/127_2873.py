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
		result += 'U'*(h-1)+'R'+'D'*(h-1)+'R'
	print(result[:-1])
else : 
	minValue = happyPoints[0][1]
	minPoint = [0,1]
	for i in range(h):
		for j in range(w//2):
			value = happyPoints[i][2*j+(i+1)%2]
			if value < minValue :
				minValue = value
				minPoint[0] = i
				minPoint[1] = 2*j+(i+1)%2
	print(minValue, minPoint)
	minPointPassed = False
	# 빠지는 게 없을 때 알고리즘
	for i in range(h//2):
		if minPoint[0]//2 == i :
			for j in range(w//2):
				if minPoint[1]//2 == j :
					if minPoint[1]%2==0:
						result += 'RDR'
					else :
						result += 'DRR'
					minPointPassed = True
				else :
					if minPointPassed :
						result += 'URDR'
					else :
						result += 'DRUR'
			result = result[:-1]+'D'
		else :
			if not minPointPassed :
				result += 'R'*(w-1)+'D'+'L'*(w-1)+'D'
			else :
				result += 'L'*(w-1)+'D'+'R'*(w-1)+'D'
	print(result[:-1])