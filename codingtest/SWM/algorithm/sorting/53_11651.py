# https://www.acmicpc.net/problem/11651

n = int(input())
coordinateList = []
for _ in range(n):
    coordinateList.append(list(map(int,input().split())))
for coordinate in sorted(coordinateList, key=lambda x:(x[1], x[0])):
    print(f'{coordinate[0]} {coordinate[1]}')
