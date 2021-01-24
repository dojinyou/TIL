# https://www.acmicpc.net/problem/2751

import sys

n = int(sys.stdin.readline())
numList = [int(sys.stdin.readline()) for _ in range(n)]
for num in sorted(numList):
    print(num)
