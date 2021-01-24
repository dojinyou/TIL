# https://www.acmicpc.net/problem/10989

import sys

n = int(sys.stdin.readline())
countList = [0]*10001
for _ in range(n) :
    countList[int(sys.stdin.readline())] += 1
for i,c in enumerate(countList):
    [print(i) for _ in range(c)]