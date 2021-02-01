# https://www.acmicpc.net/problem/11005

n, b = map(int, input().split())
result = ''
while n >= b :
	remainder = n % b
	n //= b
	if remainder >= 10 :
		remainder = chr(remainder+55)
	result = str(remainder)+result
if n >= 10 :
	n = chr(n+55)
print(str(n)+result)