from sys import stdin, maxsize
input = stdin.readline

N = int(input())
locations = list(map(int,input().split()))
locations.sort()

print(locations[(N-1)//2])