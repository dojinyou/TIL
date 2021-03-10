from sys import stdin
input=stdin.readline

N, K = map(int,input().split())
course_length = list(map(int, input().split()))
course_stack = [0]*(2*N)
for i in range(2*N):
	index = (-1)**(i//N)*(i%N+i//N)+(N*(i//N))
	course_stack[i] = course_stack[i-1] + course_length[index]
for i, stack in enumerate(course_stack):
	if K < stack :
		print((-1)**(i//N)*(i%N+i//N)+(N*(i//N))+1)
		break