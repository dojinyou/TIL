from copy import deepcopy
from sys import stdin
input=stdin.readline

N, K = map(int,input().split())
virus_box = [list(map(int, input().split())) for _ in range(N)]
virus_locations = [[] for _ in range(K)]
for i in range(N):
	for j in range(N):
		if virus_box[i][j] == 0 :
			continue
		virus_locations[virus_box[i][j]-1].append((i,j))

s,x,y = map(int,input().split())
salt = [1,-1]

for _ in range(s):
	cnt = 0
	for locations in deepcopy(virus_locations) :
		cnt += len(locations)
		for v_x,v_y in locations :
			for dx in salt :
				if (0 <= v_x+dx <= N-1) and (virus_box[v_x+dx][v_y] == 0 ):
					virus_box[v_x+dx][v_y] = virus_box[v_x][v_y]
					virus_locations[virus_box[v_x][v_y]-1].append((v_x+dx,v_y))
			for dy in salt :
				if (0 <= v_y+dy <= N-1) and (virus_box[v_x][v_y+dy] == 0 ):
					virus_box[v_x][v_y+dy] = virus_box[v_x][v_y]
					virus_locations[virus_box[v_x][v_y]-1].append((v_x,v_y+dy))
	if cnt == N*N :
		break
print(virus_box[x-1][y-1])