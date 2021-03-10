from sys import stdin
input = stdin.readline

N, M, H = map(int, input().split())
counts = [0]*(H+1)
for _ in range(N):
	counts[0] += 1
	for i in list(map(int,input().split())):
		if i <= H:
			counts[i] += 1






print(cnt%10007)