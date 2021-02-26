# https://www.acmicpc.net/problem/10819

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = permutations(list(map(int, input().split())))

result = 0
for a in arr :
	result = max(result, sum([abs(a[i]-a[i+1]) for i in range(N-1)]))
print(result)
