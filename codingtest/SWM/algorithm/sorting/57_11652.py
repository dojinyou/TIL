# https://www.acmicpc.net/problem/11652

n = int(input())
countDic = {}
for _ in range(n):
    num = int(input())
    if num in countDic.keys():
        countDic[num] += 1
    else :
        countDic[num] = 1

print(sorted(countDic.items(), key=lambda x:(-x[1], x[0]))[0][0])