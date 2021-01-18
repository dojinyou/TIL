# https://www.acmicpc.net/problem/11720

n = input()
text = input()
result = 0
for i, c in enumerate(text):
    result += int(c)
print(result)