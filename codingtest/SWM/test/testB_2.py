from sys import stdin
input=stdin.readline

N = int(input().rstrip())
powers = list(map(int,input().split()))

# 가장 긴 감소수열의 길이를 구해서 전체 길이에서 뺀다.
LCS = [1]*N
for i in range(N):
	# print(f'i={i}')
	max_length = 0
	for j in range(i):
		if powers[j] > powers[i] and LCS[j] > max_length :
			# print(f'max_length={LCS[j]}, j={j}')
			max_length = LCS[j]
	LCS[i] = max_length + 1
# print(LCS)
print(N-max(LCS))