# https://www.acmicpc.net/problem/10610

import sys
input = sys.stdin.readline

N = list(input().rstrip('\n'))
if "0" not in N : # 10의 배수가 아니라면 O(n)
	print(-1)
elif sum(map(int,N)) % 3 != 0 : # 3의 배수가 아니라면 O(n)
	print(-1)
else :
	sortedN = sorted(N,reverse=True) # O(nlogn)
	print(int(''.join(sortedN))) #O(n)