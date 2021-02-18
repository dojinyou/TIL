# https://www.acmicpc.net/problem/11728

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nArray = list(map(int, input().split()))
mArray = list(map(int, input().split()))
i, j = 0, 0
while i < n and j < m :
	if nArray[i] <= mArray[j] :
		print(nArray[i], end=' ')
		i += 1 
	else :
		print(mArray[j], end=' ')
		j += 1

array = nArray[i:] if j==m else mArray[j:]
for item in array :
	print(item, end=' ')
