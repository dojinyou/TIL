# 16분 점프 점프
# https://www.acmicpc.net/problem/18512

from math import gcd
from sys import stdin
input = stdin.readline

x, y, s1, s2 = map(int,input().split())
# 안 만나는 경우
def lcm(x,y):
	return x*y//gcd(x,y)
max_length = lcm(x,y)
location1 = s1
location2 = s2
is_meet = False
while location1 < s1+max_length or location2 < s2+max_length :
	if location1 == location2 :
		print(location1)
		is_meet = True
		break
	if location1 < location2 :
		location1 += x
	elif location2 < location1:
		location2 += y
if not is_meet :
	print(-1)