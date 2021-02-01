# https://www.acmicpc.net/problem/1373

n = input()
n = n[::-1]
result = ''
for i in range(0, len(n),3):
	num = 0
	for i,c in enumerate(n[i:i+3]):
		num += int(c)*(2**i)
	result = str(num) +result
print(result)