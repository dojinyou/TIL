# https://www.acmicpc.net/problem/9012

from sys import stdin

n = int(stdin.readline())
for _ in range(n):
	PS = stdin.readline()
	stack = []
	isVPS = True
	
	for c in PS :
		if c == "(":
			stack.append(c)
		elif c == ")":
			if len(stack) == 0 :
				isVPS = False
				break
			stack.pop()

	if len(stack) != 0:
		isVPS = False

	print("YES" if isVPS else "NO")


