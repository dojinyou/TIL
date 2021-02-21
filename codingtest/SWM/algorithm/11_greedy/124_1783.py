# https://www.acmicpc.net/problem/1783

import sys
input = sys.stdin.readline

h, w = map(int,input().split())
if h == 1 or w == 1:
	print(1)
elif h == 2:
	if w >= 7 :
		print(4)
	else :
		print((w-1)//2+1)
elif w == 2 :
	print(2)
else :
	if w >= 7 :
		print(w-2)
	else :
		print(3+w//4)
