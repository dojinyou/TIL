from itertools import permutations
from sys import stdin
input = stdin.readline

N, K = map(int,input().split())
kit = list(map(int,input().split()))
cnt = 0
for order in permutations(kit):
	weight = 500
	is_possible = True
	for ex in order :
		weight += ex
		weight -= K
		if weight < 500 :
			is_possible = False
			break
	if is_possible :
		cnt += 1
print(cnt)

