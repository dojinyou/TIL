from sys import stdin
input = stdin.readline

def get_boomerang(x,y,direction):
	if direction == 0 :
		if x+1 < M and y+1 < N :
			return (board[x][y]*2+board[x+1][y]+board[x][y+1], set([(x,y),(x+1,y),(x,y+1)]))
	elif direction == 1:
		if 0 <= x-1 and y+1 < N :
			return (board[x][y]*2+board[x-1][y]+board[x][y+1], set([(x,y),(x-1,y),(x,y+1)]))
	elif direction == 2:
		if 0 <= x-1 and 0 < y-1 :
			return (board[x][y]*2+board[x-1][y]+board[x][y-1], set([(x,y),(x-1,y),(x,y-1)]))
	elif direction == 3:
		if x+1 < M and 0 < y-1 :
			return (board[x][y]*2+board[x+1][y]+board[x][y-1], set([(x,y),(x+1,y),(x,y+1)]))


N, M = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(M)]

data = []
for i in range(M):
	for j in range(N):
		for k in range(4):
			boomerang = get_boomerang(i,j,k)
			if boomerang :
				data.append(boomerang)

sorted_data = sorted(data, key=lambda x:x[0], reverse=True)
max_value = 0
for i in range(len(sorted_data)):
	cur_value = 0
	cur_set = set()
	for value, locations in sorted_data[i:]:
		if len(cur_set.intersection(locations)) == 0 :
			cur_set.update(locations)
			cur_value += value
	max_value = max(max_value, cur_value)
print(max_value)