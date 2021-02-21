# https://www.acmicpc.net/problem/2875

import math
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

maxNumOfTeams = min(n//2, m)
numOfPeopleLeft = (n + m) - 3*maxNumOfTeams
gap = k - numOfPeopleLeft
if gap > 0 :
	maxNumOfTeams -= math.ceil(gap/3)
print(maxNumOfTeams if maxNumOfTeams >= 0 else 0)
