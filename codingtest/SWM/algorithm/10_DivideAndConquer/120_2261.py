# https://www.acmicpc.net/problem/2261

import sys
input = sys.stdin.readline

n = int(input().rstrip())
points = [tuple(map(int,input().split())) for _ in range(n)]

points.sort()

def getMinDistance(array, startIndex, endIndex):
	size = endIndex - startIndex + 1
	minDistance = (array[startIndex][0]-array[startIndex+1][0])**2+(array[startIndex][1]-array[startIndex+1][1])**2
	if size <= 3 :
		for i in range(size):
			for j in range(i+1,size):
				distance = (array[startIndex+i][0]-array[startIndex+j][0])**2+(array[startIndex+i][1]-array[startIndex+j][1])**2
				if distance < minDistance :
					minDistance = distance
		return minDistance
		
	mid = (startIndex+endIndex) // 2
	leftPointsMinDistance = getMinDistance(array, startIndex, mid)
	rightPointsMinDistance = getMinDistance(array, mid+1, endIndex)

	d = min(leftPointsMinDistance,rightPointsMinDistance)

	centerPoints = []
	for i in range(startIndex,endIndex+1):
		dx = array[i][0] - array[mid][0]
		if dx**2 < d :
			centerPoints.append(array[i])
	
	centerPoints = sorted(centerPoints, key=lambda x : x[1])

	for i in range(len(centerPoints)):
		for j in range(i+1,len(centerPoints)):
			dy = centerPoints[i][1] - centerPoints[j][1]
			if dy**2 < d :
				distance = dy**2 + (centerPoints[i][0] - centerPoints[j][0])**2
				if distance < d:
					d = distance
			else :
				break
	
	return d

print(getMinDistance(points, 0, n-1))