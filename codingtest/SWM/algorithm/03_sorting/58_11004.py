# https://www.acmicpc.net/problem/11004

n, k= map(int,input().split())
numList = list(map(int,input().split()))
print(sorted(numList)[k-1])