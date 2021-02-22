# https://www.acmicpc.net/problem/11662

import math
import sys
input = sys.stdin.readline

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())
# t초 뒤에 민호의 위치 = (a, b), 강호의 위치 = (c,d), 둘 사이의 거리는 math.sqrt((a-c)**2+(b-d)**2)
def getDistance(t,T):
	a = (Bx*t+Ax*(T-t))/T
	b = (By*t+Ay*(T-t))/T
	c = (Dx*t+Cx*(T-t))/T
	d = (Dy*t+Cy*(T-t))/T
	distance = math.sqrt((a-c)**2+(b-d)**2)
	return distance

T = 1e11
l = 0
r = T
minDistaince = getDistance(0,T)
for i in range(100):
	a = (2*l+r)//3
	b = (l+2*r)//3
	if getDistance(a,T) > getDistance(b,T):
		l = a
	else :
		r = b
print(f'{getDistance((l+r)//2,T):.10f}')


