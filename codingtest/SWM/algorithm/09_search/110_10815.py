# https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

# def binarySearch(c):
# 	l = 0
# 	r = n-1
# 	while l <= r :
# 		t = (r+l)//2
# 		if cards[t] == c :
# 			return 1
# 		elif cards[t] > c :
# 			r = t - 1
# 		else :
# 			l = t + 1
# 	return 0


# n = int(input())
# cards = list(map(int, input().split()))
# m = int(input())
# check = list(map(int, input().split()))

# cards.sort()
# for c in check :
# 	print(binarySearch(c), end=' ')
cards = {}
n = int(input())
for i in list(map(int, input().split())):
	cards[i] = 1
m = int(input())
for c in list(map(int, input().split())):
	try :
		print(cards[c], end=' ')
	except :
		print(0, end=' ')
