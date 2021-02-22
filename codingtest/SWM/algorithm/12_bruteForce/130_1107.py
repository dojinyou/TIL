# https://www.acmicpc.net/problem/1107

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(int,input().split()))
if n > 97 and n < 103 :
	print(abs(n-100))
elif m == 0 :
	print(1)
elif m == 10 :
	print(abs(m-100))
else :
	strN = str(n)
	buttons = []
	for i in range(10):
		if i not in broken :
			buttons.append(i)
	value =[[]]
	for c in strN :
		for i, button in enumerate(buttons) :
			maxIndex = 0
			if int(c) >= button :
				maxIndex = i
		
				


