# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

def getTreeLength(h, trees, index):
	s = 0
	for i in range(index,len(trees)):
		s += max(0, trees[i]-h)
	return s

def getStartIndex(h, trees):
	s = 0
	e = len(trees)
	startIndex = 0
	while s+1 < e :
		t = (s+e)//2
		if trees[t] <= h :
			startIndex = t
			s = t
		else :
			e = t
	return startIndex

n, m = map(int, input().split())
trees =list(map(int, input().split()))
trees.sort()

s = 0
e = max(trees)
result = 0

while s+1 < e :
	t = (s+e)//2
	startIndex = getStartIndex(t,trees)
	# print(f's={s}, e={e}, t={t}, startIndex={startIndex}, result={result}')
	if getTreeLength(t,trees, startIndex) >= m:
		result = t
		s = t
	else :
		e = t

startIndex = getStartIndex(e,trees)
result = t if getTreeLength(e,trees,startIndex) >= m else result
print(result)
