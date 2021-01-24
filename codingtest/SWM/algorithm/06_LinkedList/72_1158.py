# https://www.acmicpc.net/problem/1158

import sys
from collections import deque

n, k = map(int,sys.stdin.readline().rstrip("\n").split())
array = [i+1 for i in range(n)]
removeIndex = k-1
mod = n
result = []
for _ in range(n):
	result.append(str(array.pop(removeIndex)))
	if mod != 1 :
		mod -= 1
		removeIndex = (removeIndex+k-1)%mod
print(f'<{", ".join(result)}>')