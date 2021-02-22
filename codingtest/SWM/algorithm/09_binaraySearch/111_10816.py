# https://www.acmicpc.net/problem/10816

# import sys
# input = sys.stdin.readline

# n = int(input())
# cards = {}
# for card in list(map(int, input().split())):
# 	try:
# 		cards[card] += 1
# 	except :
# 		cards[card] = 1
# m = int(input())
# for c in list(map(int, input().split())):
# 	try :
# 		print(cards[c], end=' ')
# 	except :
# 		print(0, end=' ')

# Lower Bound / Upper Bound

import sys
input = sys.stdin.readline

def getLowerBound(array, value):
	low = 0
	high = len(array)
	while (low < high) :
		mid = (low+high)//2
		if value <=array[mid] :
			high = mid
		else :
			low = mid + 1
	return low

def getUpperBound(array, value):
	low = 0
	high = len(array)
	while (low < high):
		mid = (low+high)//2
		if value >= array[mid] :
			low = mid + 1
		else :
			high = mid
	return low

n = int(input())
cards = list(map(int, input().split()))
cards.sort()
print(f'-----------------\n{cards}\n-----------------------')
m = int(input())
for c in list(map(int, input().split())):
	print(f'c = {c}, upper = {getUpperBound(cards, c)}, lower = {getLowerBound(cards,c)}')
	# print(getUpperBound(cards, c) - getLowerBound(cards,c), end=' ')
