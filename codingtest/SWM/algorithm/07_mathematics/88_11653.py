# https://www.acmicpc.net/problem/11653

import sys

inputNum = int(sys.stdin.readline())
n = inputNum
div = 2
while n != 1 :
	if n % div == 0 :
		print(div)
		n //= div
	else :
		div += 2 if div != 2 else 1
