# https://www.acmicpc.net/problem/1517

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
swap = 0

def mergeSort(array, s, e):
	global swap
	if s + 1 < e :
		mid = (s+e)//2
		# print(s,e,mid)
		sortedLeftArray = mergeSort(array,s,mid)
		sortedRightArray= mergeSort(array,mid,e)
		i = 0
		j = 0
		newArray = [0]*(e-s)
		# print(f'sortedLeftArray = {sortedLeftArray}')
		# print(f'sortedRightArray = {sortedRightArray}')
		for k in range(e-s):
			# print(f'k={k}, i={i}, j={j}')
			if  i < mid-s and (j == e-mid or sortedLeftArray[i] <= sortedRightArray[j]):
				newArray[k] = sortedLeftArray[i]
				i += 1
			else :
				newArray[k] = sortedRightArray[j]
				# print(f'newArray = {newArray}, k={k}')
				# print(f'rightArray = {sortedRightArray}, j={j}')
				if k < mid+j :
					swap += mid+j-k-s
					# print(f'swap={swap}')
				j += 1
	else :
		newArray = array[s:e]
	return newArray
mergeSort(array,0,n)
print(swap)