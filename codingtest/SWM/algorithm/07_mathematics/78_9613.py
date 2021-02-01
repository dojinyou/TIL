# https://www.acmicpc.net/problem/9613

import math

n = int(input())
for _ in range(n):
	numList = list(map(int, input().split()))[1:]
	gcdSet = []
	for i, origin in enumerate(numList):
		for j, other in enumerate(numList[i+1:]):
			gcdSet.append(math.gcd(origin,other))
	print(sum(gcdSet))
