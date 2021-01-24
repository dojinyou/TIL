# https://www.acmicpc.net/problem/1406

import sys
from collections import deque

text = sys.stdin.readline().rstrip("\n")
deque_L = deque(text)
deque_R = deque()
n = int(sys.stdin.readline())
for _ in range(n):
	print(deque_L, deque_R)
	order = sys.stdin.readline().split()
	if order[0] == "L" :
		if len(deque_L) != 0 :
			deque_R.appendleft(deque_L.pop())
	if order[0] == "D" :
		if len(deque_R) != 0:
			deque_L.append(deque_R.popleft())
	elif order[0] == "B" :
		if len(deque_L) != 0 :
			deque_L.pop()
	elif order[0] == "P" :
		deque_L.append(order[1])
deque_L.extend(deque_R)
print("".join(map(str,deque_L)))