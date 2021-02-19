# https://www.acmicpc.net/problem/2261

import sys
input = sys.stdin.readline

n = int(input().rstrip())
points = [tuple(map(int,input().split())) for _ in range(n)]

print(sorted(points))
# 두 점의 거리는 (Bx-Ax)**2+(By-Ay)**2