from collections import deque
from sys import stdin
input = stdin.readline

N, M, K, X = map(int, input().split())
loads = [[] for _ in range(N+1)]
for _ in range(M):
	x, y = map(int, input().split())
	loads[x].append(y)

visited = [False]*(N+1)
visited[X] = True
answer = []
q = deque([(X,0)])
while q :
	city, distance = q.popleft()
	if distance == K :
		answer.append(city)
	for next_city in loads[city]:
		if not visited[next_city] :
			visited[next_city] = True
			q.append((next_city,distance+1))
if len(answer) == 0 :
	print(-1)
else :
	for city in sorted(answer) :
		print(city)

	