# from sys import stdin
# input = stdin.readline

N, K = input().rstrip().split()
k_list = input().rstrip().split()
k_list.sort(reverse=True)
answer = ""
is_under = False
for i, num in enumerate(N) :
	for k in k_list :
		if is_under or num == k :
			answer += k
			break
		elif num > k :
			answer += k
			is_under = True
			break
	if len(answer) == 0 :
		is_under = True
print(answer)

# def DFS(val):
# 	if len(val) == len(str(N)):
# 		if int(val) <= N :
# 			return val
# 		else : return 0
# 	for el in data :
# 		temp = DFS(val + str(el))
# 		if temp:
# 			return temp
# N, K = map(int, input().split())
# data = list(map(int,input().split()))
# data.sort(reverse=True)

# is_digit = False
# for el in data :
# 	if int(str(N)[0]) >= el :
# 		is_digit = True
# 		break
# if is_digit:
# 	answer = DFS("")
# else :
# 	answer = str(data[0])*(len(str(N))-1)
# print(answer)