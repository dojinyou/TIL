# https://www.acmicpc.net/problem/11576

A, B = map(int, input().split())
input()
numArray = list(map(int, input().split()))
AtoT = 0
for i, num in enumerate(numArray[::-1]):
	AtoT += num * A ** i

TtoB = []
while AtoT != 0 :
	TtoB.append(str(AtoT % B))
	AtoT //= B
print(' '.join(TtoB[::-1]))