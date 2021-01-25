# https://www.acmicpc.net/problem/10430

import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
deque = deque([i for i in range(1,n+1)])
result = []
while deque :
	deque.rotate(-k+1)
	result.append(str(deque.popleft()))

sys.stdout.write(f'<{", ".join(result)}>')