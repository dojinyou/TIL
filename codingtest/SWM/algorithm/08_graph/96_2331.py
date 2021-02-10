# https://www.acmicpc.net/problem/2331

import sys
input = sys.stdin.readline

A, P = input().split()
D = [A]
while True :
	result = 0
	for c in D[-1]:
		result += int(c)**int(P)
	result = str(result)
	if result in D :
		print(D.index(result))
		break
	D.append(result)
	print(D)



