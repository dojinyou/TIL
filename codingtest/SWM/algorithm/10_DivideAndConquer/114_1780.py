# https://www.acmicpc.net/problem/1780

import numpy as np
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

def checkPaper(matrix, n):
	value = matrix[0][0]
	isPerfect = True
	for row in matrix :
		for num in row :
			if value != num :
				isPerfect = False
				break
	if isPerfect :
		result = [0, 0, 0]
		result[value+1] += 1
		return result
	else :
		n = n//3
		result = [0,0,0]
		for i in range(9):
			miniMatrix = matrix[n*(i//3):n*((i//3)+1)][n*(i%3):n*((i%3)+1)]
			print(miniMatrix)
			result = list(np.array(result)+np.array(checkPaper(miniMatrix, n)))
		return result

for i in checkPaper(matrix, n):
	print(i)