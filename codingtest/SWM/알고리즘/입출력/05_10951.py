# https://www.acmicpc.net/problem/10951
 
while True:
    try:
        print(sum(map(int,input().split())))
    except EOFError:
        break
