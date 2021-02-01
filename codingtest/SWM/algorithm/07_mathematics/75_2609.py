# https://www.acmicpc.net/problem/2609

from itertools import chain

def getDivisor(dic, num):
	for i in range(2,num+1):
		isFirst = True
		while True :
			if num % i == 0 :
				if isFirst :
					dic[i] = 1
					isFirst = False
				else :
					dic[i] += 1
				num //= i
			else :
				break
a,b = map(int, input().split())

divisor_a = {1:1}
divisor_b = {1:1}
getDivisor(divisor_a, a)
getDivisor(divisor_b, b)

# 공약수
commonDivisor = 1
for key in divisor_a:
	if key in divisor_b:
		commonDivisor *= key**min(divisor_a[key], divisor_b[key])
print(commonDivisor)

# 공배수
commonMuttiple = 1
dic = {}
for key,value in chain(divisor_a.items(), divisor_b.items()):
	if key in dic and dic[key] > value :
		continue
	dic[key] = value

for key, value in dic.items():
	commonMuttiple *= key**value
print(commonMuttiple)		


# 다른 사람 풀이1
# import math

# a, b = map(int, input().split())
# print(math.gcd(a, b))
# print(math.lcm(a, b))

# 다른 사람 풀이2
# n1, n2 = map(int,input().split(' '))

# GCD = 1
# LCM = 1
# i = 2

# while(1):
#     if(i > n1 or i > n2):
#         break;

#     if(n1 % i == 0 and n2 % i == 0):
#         GCD *= i
#         LCM *= i
#         n1 = int(n1 / i)
#         n2 = int(n2 / i)
#         i = 1

#     i += 1

# LCM = LCM * n1 * n2

# print(GCD)
# print(LCM)