# https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

n, c = map(int, input().split()) # O(1)
house = [int(input()) for _ in range(n)] # O(n)

house.sort() # O(n log n)
if c == 2:
	print(house[-1] - house[0])
else :
	gaps = [house[i+1]-house[i] for i in range(n-1)] # O(n)

	s = min(gaps) # O(n)
	e = house[-1]-house[0] # O(n)

	def getCount(g, gaps):
		count = 0
		stack = 0
		for gap in gaps :
			stack += gap
			if stack >= g :
				count += 1
				stack = 0
		return count


	result = 0
	while s <= e :
		g = (s+e)//2
		print(s,g,e,result)
		if getCount(g, gaps) >= (c-1):
			s = g + 1
			if result < g :
				result = g
		else :
			e = g - 1
	print(result)

