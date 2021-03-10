from sys import stdin
input = stdin.readline

N = int(input())
board = []
student_locations = []
teacher_locations = []
for i in range(N):
	board.append(list(map(lambda x:x if x!="X" else 0, input().rstrip().split())))
	for j in range(N):
		if board[i][j] == "S" :
			student_locations.append((i,j))
		elif board[i][j] == "T" :
			teacher_locations.append((i,j))
x_blocks = []
y_blocks = []
for x,y in teacher_locations :
	temp = []
	for i in range(y+1,N):
		temp.append((x,i))
		if board[x][i] :
			if board[x][i] == "S" :
				y_blocks.append(temp)
			break
	temp = []
	for i in range(y-1,-1,-1):
		temp.append((x,i))
		if board[x][i] :
			if board[x][i] == "S" :
				y_blocks.append(temp)
			break
	temp = []
	for i in range(x+1,N):
		temp.append((i,y))
		if board[i][y] :
			if board[i][y] == "S" :
				x_blocks.append(temp)
			break
	temp = []
	for i in range(x-1,-1,-1):
		temp.append((i,y))
		if board[i][y] :
			if board[i][y] == "S" :
				x_blocks.append(temp)
			break

if len(x_blocks)+len(y_blocks) <= 3 :
	print("YES")
elif len(x_blocks) > 3 or len(y_blocks) > 3 :
	print("NO")
else :
	cnt = len(x_blocks)+len(y_blocks)
	check_y = []
	for x_block in x_blocks :
		for i,y_block in enumerate(y_blocks) :
			if i in check_y :
				continue
			is_dubble_block = False
			for x_x, x_y in x_block :
				for y_x, y_y in y_block :
					if x_x == y_x and x_y == y_y :
						is_dubble_block = True
						check_y.append(i)
						cnt -= 1
						break
				if is_dubble_block:
					break
	if cnt <= 3 :
		print("YES")
	else :
		print("NO")

