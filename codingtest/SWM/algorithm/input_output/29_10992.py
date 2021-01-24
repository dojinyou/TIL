# https://www.acmicpc.net/problem/10992
n = int(input())
for i in range(1,n+1):
	if i == 1 :
		print(f'{" "*(n-i)}*')
	elif i == n :
		print(f'{"*"*(2*i-1)}')
	else :
		print(f'{" "*(n-i)}*{" "*(2*(i-1)-1)}*')