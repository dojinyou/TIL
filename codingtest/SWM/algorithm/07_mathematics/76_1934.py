# https://www.acmicpc.net/problem/1934

import math

n = int(input())
for _ in range(n):
	a ,b = map(int, input().split())
	print(math.lcm(a,b))