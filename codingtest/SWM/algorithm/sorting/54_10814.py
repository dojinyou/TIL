# https://www.acmicpc.net/problem/10814

import sys

n = int(sys.stdin.readline())
coordinateList = []
for _ in range(n):
    coordinateList.append(list(map(int,sys.stdin.readline().split())))
for coordinate in sorted(coordinateList, key=lambda x:(x[1], x[0])):
    print(f'{coordinate[0]} {coordinate[1]}')
