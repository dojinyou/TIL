# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline

import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

cut_low = 0
cut_high = max(trees)
result = 0
while cut_high >= cut_low:
    pivot = int((cut_low + cut_high) / 2)
    # pivot의 길이로 자를 수 있는 나무의 총 길이
    cut_tree = sum([x - pivot if x >= pivot else 0 for x in trees])
    # 비교
    if cut_tree >= M:
        cut_low = pivot + 1
        # 이 높이로 M이상의 나무를 자를 수 있고, 저장된 정답보다 크다면 이 높이로 정답을 업데이트
        if result < pivot: result = pivot
    elif cut_tree < M: cut_high = pivot - 1

print(result)

# def getTreeLength(h, trees, startIndex, endIndex):
# 	s = 0
# 	for i in range(startIndex, endIndex):
# 		s += max(0, trees[i]-h)
# 	return s

# def getIndex(h, trees):
# 	s = 0
# 	e = len(trees)
# 	startIndex = 0
# 	while s+1 < e :
# 		t = (s+e)//2
# 		if trees[t] <= h :
# 			startIndex = t
# 			s = t
# 		else :
# 			e = t
# 	return startIndex

# n, m = map(int, input().split())
# trees =list(map(int, input().split()))
# trees.sort()

# s = 0
# e = max(trees)
# result = 0
# prevH = e
# prevIndex = len(trees)-1
# prevTreeLength = 0
# while s+1 < e :
# 	h = (s+e)//2
# 	index = getIndex(h, trees)
# 	# a < b
# 	# indexA ~ 끝까지 a로 짜르고 indexA~indexB a로 짜른고 빼준다
# 	print(prevIndex, index)
# 	if prevH < h :
# 		treeLength = prevTreeLength - getTreeLength(prevH, trees, prevIndex, index+1) - (h-prevH)*(len(trees)-1-index)
# 	# a > b
# 	# indexA ~ 끝까지 a로 짜르고 indexB~indexA b로 짜르고 더해준다.
# 	else :
# 		treeLength = prevTreeLength + getTreeLength(h, trees, index, prevIndex+1) + (prevH-h)*(len(trees)-1-prevIndex)
# 	print(s,e,h, treeLength)
# 	prevTreeLength = treeLength
# 	prevH = h
# 	prevIndex = index
# 	if treeLength >= m:
# 		result = h
# 		s = h
# 	else :
# 		e = h

# index = getIndex(e,trees)
# if prevH < h :
# 	treeLength = prevTreeLength - getTreeLength(prevH, trees, prevIndex, index+1) - (h-prevH)*(len(trees)-1-index)
# else :
# 	treeLength = prevTreeLength + getTreeLength(h, trees, index, prevIndex+1) + (prevH-h)*(len(trees)-1-prevIndex)
# result = h if treeLength >= m else result
# print(result)
