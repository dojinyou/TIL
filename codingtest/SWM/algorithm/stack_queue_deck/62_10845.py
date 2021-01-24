# https://www.acmicpc.net/problem/10845

from sys import stdin
from collections import deque

n = int(stdin.readline())
queue = deque()
for _ in range(n):
	order = stdin.readline().split()
	if order[0] == "push":
		queue.appendleft(int(order[1]))
	elif order[0] == "pop":
		if len(queue) != 0 :
			print(queue.pop())
		else :
			print("-1")
	elif order[0] == "size":
		print(len(queue))
	elif order[0] == "empty":
		print(1 if len(queue)==0 else 0)
	elif order[0] == "front":
		if len(queue) != 0 :
			print(queue[-1])
		else :
			print("-1")	
	elif order[0] == "back":
		if len(queue) != 0 :
			print(queue[0])
		else :
			print("-1")	



