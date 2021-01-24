# https://www.acmicpc.net/problem/10828

from sys import stdin

n = int(stdin.readline())
stack = []
for _ in range(n):
	order = stdin.readline().split()
	if order[0] == "push":
		stack.append(int(order[1]))
	elif order[0] == "pop":
		if len(stack) != 0 :
			print(stack.pop())
		else :
			print("-1")
	elif order[0] == "size":
		print(len(stack))
	elif order[0] == "empty":
		print(1 if len(stack)==0 else 0)
	elif order[0] == "top":
		if len(stack) != 0 :
			print(stack[-1])
		else :
			print("-1")	