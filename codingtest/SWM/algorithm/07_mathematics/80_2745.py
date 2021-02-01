# https://www.acmicpc.net/problem/2745

n, b = input().split()
b = int(b)
n = n[::-1]
result = 0
for i, c in enumerate(n):
	if not c.isdigit() :
		c = ord(c)-55
	result += int(c)*(b**i)
print(result)