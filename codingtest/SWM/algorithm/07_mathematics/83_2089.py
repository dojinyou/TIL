# https://www.acmicpc.net/problem/2089

# -2 = 10
# -1 = 11
# 0 = 0 0
# 1 = 1 1
# 2 = 110 10
# 3 = 111 11
# 4 = 100 100
# 5 = 101 101
# 6 = 11010 = 110
# 7 = 11011 = 111
# 8 = 11000 = 1000

n= int(input())
result = '0' if n == 0 else ''
while n != 0 :
	r = n % -2
	n //= -2
	n += 1 if r == -1 else 0
	result = str(-r) + result
print(result)