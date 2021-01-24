# https://www.acmicpc.net/problem/11650

n = int(input())
coordinateList = []
for _ in range(n):
    coordinateList.append(list(map(int,input().split())))
for coordinate in sorted(coordinateList, key=lambda x:(x[0], x[1])):
    print(f'{coordinate[0]} {coordinate[1]}')

# import sys
# location = {}
# for _ in range(int(sys.stdin.readline())):
#     x, y = map(int, sys.stdin.readline().split())
#     if x in location.keys() :
#         location[x].append(y)
#     else :
#         location[x] = [y]
# for x, y_list in sorted(location.items()):
#     for y in sorted(y_list):
#         print(x, y)
