# https://www.acmicpc.net/problem/6588

import sys

numArray = []
while True :
	inputNum = int(sys.stdin.readline())
	if inputNum == 0 :
		break
	numArray.append(inputNum)

maxValue = max(numArray)
isPrime = [True]*(maxValue+1)
isPrime[0], isPrime[1] = False, False
primeArray = []
for i in range(3,maxValue+1):
	if isPrime[i]:
		primeArray.append(i)
		for j in range(2*i, maxValue+1, i):
			isPrime[j] = False

for i in numArray:
	isFinished = False
	for pNum in primeArray:
		if isPrime[i-pNum] :
			sys.stdout.write(f'{i} = {pNum} + {i-pNum}\n')
			isFinished = True
			break
	if not isFinished :
		sys.stdout.write("Goldbach's conjecture is wrong.\n")


