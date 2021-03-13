from sys import stdin
input = stdin.readline

N = input().rstrip()

s = 0
for i, num in enumerate(N) :
	if i < len(N)//2 :
		s+=int(num)
	else :
		s-=int(num)
if s == 0 :
	print("LUCKY")
else :
	print("READY")