from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

cnt_sec = 0
cnt_hour = 0
for i in range(60):
	if str(K) in str(i) :
		cnt_sec += 1
for i in range(N):
	if i < 10 :
		i = "0"+str(i)
	if str(K) in str(i) :
		cnt_hour += 1
print(cnt_hour*3600+(N+1-cnt_hour)*(120-cnt_sec)*cnt_sec)


# 완전 탐색
# h,m,s = 0,0,0
# cnt = 0
# while True :
# 	if str(K) in f'{str(h).zfill(2)}{str(m).zfill(2)}{str(s).zfill(2)}' :
# 		print(f'{str(h).zfill(2)}{str(m).zfill(2)}{str(s).zfill(2)}')
# 		cnt += 1
# 	s += 1
# 	if s == 60 :
# 		s = 0
# 		m += 1
# 		if m == 60 :
# 			m = 0
# 			h += 1
# 			if h == N+1 :
# 				break
# print(cnt)