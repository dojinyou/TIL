# https://www.acmicpc.net/problem/1451

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
sq = [[] for _ in range(H)]
for i in range(H):
	for c in input().rstrip('\n'):
		sq[i].append(int(c))
# print(sq)
result = 0

# 세로로 3개
for i in range(1,W-1):
	for j in range(i+1,W):
		s1 = sum([sq[a][b] for a in range(H) for b in range(i)])
		s2 = sum([sq[a][b] for a in range(H) for b in range(i,j)])
		s3 = sum([sq[a][b] for a in range(H) for b in range(j,W)])
		result = max(result, s1*s2*s3)
# 가로로 3개
for i in range(1,H-1):
	for j in range(i+1,H):
		s1 = sum([sq[a][b] for a in range(i) for b in range(W)])
		s2 = sum([sq[a][b] for a in range(i,j) for b in range(W)])
		s3 = sum([sq[a][b] for a in range(j,H) for b in range(W)])
		result = max(result, s1*s2*s3)
# 위1 아래 2
for i in range(H):
	for j in range(W):
		s1 = sum([sq[a][b] for a in range(i) for b in range(W)])
		s2 = sum([sq[a][b] for a in range(i,H) for b in range(j)])
		s3 = sum([sq[a][b] for a in range(i,H) for b in range(j,W)])
		result = max(result, s1*s2*s3)
# 위2 아래 1
for i in range(H):
	for j in range(W):
		s1 = sum([sq[a][b] for a in range(i) for b in range(j)])
		s2 = sum([sq[a][b] for a in range(i) for b in range(j,W)])
		s3 = sum([sq[a][b] for a in range(i,H) for b in range(W)])
		result = max(result, s1*s2*s3)
# 왼1 오른2
for i in range(H):
	for j in range(W):
		s1 = sum([sq[a][b] for a in range(H) for b in range(j)])
		s2 = sum([sq[a][b] for a in range(i) for b in range(j,W)])
		s3 = sum([sq[a][b] for a in range(i,H) for b in range(j,W)])
		result = max(result, s1*s2*s3)
# 왼2 오른1
for i in range(H):
	for j in range(W):
		s1 = sum([sq[a][b] for a in range(i) for b in range(j)])
		s2 = sum([sq[a][b] for a in range(i,H) for b in range(j)])
		s3 = sum([sq[a][b] for a in range(H) for b in range(j,W)])
		result = max(result, s1*s2*s3)
print(result)
