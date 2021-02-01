# https://www.acmicpc.net/problem/1212

EtoT = {"0":"000","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
n = input()
if n == '0' :
	print('0')
else :
	result = ''
	for i, c in enumerate(n):
		result += EtoT[c] if i != 0 else EtoT[c].lstrip("0")
	print(result)