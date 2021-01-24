# https://www.acmicpc.net/problem/11721

text = input()
n = len(text)//10 + 1
for i in range(n):
    startIndex = i*10
    endIndex = (i+1)*10
    print(text[startIndex:endIndex])