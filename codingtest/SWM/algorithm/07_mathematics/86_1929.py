# https://www.acmicpc.net/problem/1929


m, n = map(int, input().split())

isPrime = [True]*(n+1)
isPrime[0], isPrime[1] = False, False

for i in range(2,n+1):
	if isPrime[i]:
		for j in range(2*i, n+1, i):
			isPrime[j] = False
for i in range(m, n+1):
	if isPrime[i]:
		print(i)

