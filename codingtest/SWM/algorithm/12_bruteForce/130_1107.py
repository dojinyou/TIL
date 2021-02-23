# https://www.acmicpc.net/problem/1107

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = list(map(int,input().split()))
buttons = list(range(10))
for i in broken :
	buttons.remove(i)
	
min_count = abs(N-100)
for num in range(1000001):
	num = str(num)
	is_possible = True
	for n in num :
		if int(n) not in buttons :
			is_possible = False
			break
	if is_possible :
		min_count = min(min_count, abs(N-int(num))+len(num))
print(min_count)