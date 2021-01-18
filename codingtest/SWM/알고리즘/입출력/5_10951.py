# https://www.acmicpc.net/submit/10951
 
while True:
    try:
        print(sum(map(int,input().split())))
    except EOFError:
        break
