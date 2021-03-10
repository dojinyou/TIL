from sys import stdin
input = stdin.readline

N, K = input().rstrip().split()
set_k = input().rstrip().split()
set_k.sort(reverse=True)
answer = ""
is_under = False
for i in N :
	for k in set_k :
		if is_under or i == k :
			answer += k
			break
		elif i > k :
			answer += k
			is_under = True
			break
print(answer)