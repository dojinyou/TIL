from sys import stdin
input = stdin.readline

N, M, H = map(int, input().split())
students = [list(map(int,input().split())) for _ in range(N)]
counts = [0]*(H+1)
counts[0] = 1
for student in students:
	data = []
	for i in range(H+1):
		for block in student:
			if counts[i] and i+block <= H:
				data.append([i+block, counts[i]])
	for h, count in data :
		counts[h] = (counts[h]+count)%10007
print(counts[H])