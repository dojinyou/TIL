# https://www.acmicpc.net/problem/1978

def isPrimeNumber(n):
	if n == 1 :
		return False
	for i in range(2,n):
		if n % i == 0 :
			return False
	return True
result = 0
input()
for i in list(map(int, input().split())):
	if isPrimeNumber(i):
		result += 1

print(result)