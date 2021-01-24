# https://www.acmicpc.net/problem/10991

n = int(input())
for i in range(1,n+1):
	print(f'{" "*(n-i)}{"*"*(i)}')