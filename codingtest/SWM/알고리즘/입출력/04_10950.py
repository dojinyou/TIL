# https://www.acmicpc.net/problem/10950
 
n = int(input())

for _ in range(n):
    inputList = input().split(" ")
    print(sum(map(int, inputList)))