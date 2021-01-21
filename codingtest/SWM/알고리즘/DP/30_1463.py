# https://www.acmicpc.net/problem/1463

from collections import deque
n = int(input())
deque = deque([1])
cnt_list = [n]*(n+1)
cnt_list[1]=0

while len(deque) > 0 :
	nextIndex = deque.pop()
	if nextIndex == n :
		break
	if cnt_list[nextIndex+1] > cnt_list[nextIndex]+1 :
		cnt_list[nextIndex+1] = cnt_list[nextIndex]+1
		deque.appendleft(nextIndex+1)
	try :
		if cnt_list[nextIndex*2] > cnt_list[nextIndex]+1 :
			cnt_list[nextIndex*2] = cnt_list[nextIndex]+1
			deque.appendleft(nextIndex*2)
		if cnt_list[nextIndex*3] > cnt_list[nextIndex]+1 :
			cnt_list[nextIndex*3] = cnt_list[nextIndex]+1
			deque.appendleft(nextIndex*3)
	except :
		pass
print(cnt_list[n])


