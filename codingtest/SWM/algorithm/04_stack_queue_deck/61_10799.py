# https://www.acmicpc.net/problem/10799

from sys import stdin

PS = stdin.readline()
prev = "("
pipes = 0
frac = 0
for c in PS[1:]:
	if c == "(" :
		if prev == "(" :
			pipes += 1
	elif c == ")":
		if prev=="(" :
			frac += pipes
		elif prev==")":
			pipes -= 1
			frac += 1
	prev = c
	
print(frac)



