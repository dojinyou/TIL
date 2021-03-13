from collections import deque
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
waters_info = deque()
locations = {}
for water_location in list(map(int, input().split())):
	waters_info.append((water_location,-1))
	waters_info.append((water_location,1))
	locations[water_location] = True
unhappy_point = 0
while K > 0:
	water_location, dist = waters_info.popleft()
	next_house_location = water_location+dist
	if not locations.get(next_house_location):
		locations[next_house_location] = True
		unhappy_point += abs(dist)
		K -= 1
		dist = dist + 1 if dist > 0 else dist - 1
		waters_info.append((water_location, dist))
print(unhappy_point)
		
		


	

