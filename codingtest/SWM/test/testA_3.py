from sys import stdin
from collections import deque
input = stdin.readline
def get_min_count(root,target):
	# print(f'get_min_count start, root = {root}, target = {target}')
	steps = ((+2,+1),(+2,-1),(+1,+2),(+1,-2),(-1,+2),(-1,-2),(-2,+1),(-2,-1))
	root.extend([0])
	q = deque([root])
	while q :
		location = q.popleft()
		# print(f'location = {location}')
		if location[0] == target[0] and location[1] == target[1] :
			# print(f"명중, num = {location[2]}")
			return location[2]
		for step in steps :
			q.append([location[0]+step[0], location[1]+step[1], location[2]+1])


N,M = map(int, input().split())
k_location = list(map(int,input().split()))
answer = []
for _ in range(M):
	e_location = tuple(map(int,input().split()))
	# print(f'k={k_location}, e={e_location}')
	answer.append(get_min_count(k_location, e_location))
for a in answer :
	print(a, end=" ")


