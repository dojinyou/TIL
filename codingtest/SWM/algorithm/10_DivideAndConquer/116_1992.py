# https://www.acmicpc.net/problem/1992

import sys
input = sys.stdin.readline

n = int(input())
data = [input().rstrip('\n') for _ in range(n)]

def check(data,n,x,y):
	if n == 1:
		return True
	value = data[x][y]
	for i in range(n):
		for j in range(n):
			print(f'value={value}, data={data[x+i][y+j]}, x+i={x+i}, y+j={y+j}')
			if value != data[x+i][y+j]:
				return False
	return True

def getQuadTree(data, n, x, y):
	if check(data,n,x,y):
		print(f'data={data},n={n},x={x},y={y},True 나옴')
		return data[x][y]
	result = "("
	for i in range(2):
		for j in range(2):
			result += getQuadTree(data, n//2, x+i*n//2, y+j*n//2)
	result += ")"
	return result

print(getQuadTree(data,n,0,0))