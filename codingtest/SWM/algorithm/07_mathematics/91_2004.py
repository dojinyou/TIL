# https://www.acmicpc.net/problem/2004

def divCountNum(N, num):
	count = 0
	divNum = num
	while(N>=divNum):
		count += N//divNum
		divNum *= num
	return count

n, m = map(int, input().split())
print(min(divCountNum(n,5)-divCountNum(m,5)-divCountNum(n-m,5),divCountNum(n,2)-divCountNum(m,2)-divCountNum(n-m,2)))