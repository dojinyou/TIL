# https://www.acmicpc.net/problem/2446


n = int(input())
for i in range(n):
	print(f'{" "*(n-1-i)}*',end="")
	for j in range(i):
		print(f' *',end="")
	print()