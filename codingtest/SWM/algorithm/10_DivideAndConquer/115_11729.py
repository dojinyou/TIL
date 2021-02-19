# https://www.acmicpc.net/problem/11729

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
def hanoi(start, target, other, h):
	if h == 1 :
		string = f'{start} {target}\n'
		return (1, string)
	else :
		cnt, string = hanoi(start, other, target, h-1)
		cnt += 1
		string += f'{start} {target}\n'
		cnt2, string2 = hanoi(other, target, start, h-1)
		cnt += cnt2
		string += string2
		return (cnt, string)
for i in hanoi(1,3,2,n):
	print(i if type(i) is int else i.rstrip('\n'))

