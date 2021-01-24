# https://www.acmicpc.net/problem/2442

n = int(input())
for i in range(n):
	print(f'{" "*(n-i-1)}{"*"*(2*i+1)}')