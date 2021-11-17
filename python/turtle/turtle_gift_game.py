from random import randint
from turtle import TurtleScreen,RawTurtle,TK
import turtle as t


def show_init():
	def set_init_handler():
		"""
		set_init_handler 함수에 대한 설명
		: 초기 화면 관련 이벤트 처리에 대한 정의를 하는 함수
		"""
		global screen

		# 마우스모드
		# 마우스 클릭시 이벤트 발생을 통한 lobby 보여주는 함수 호출
		screen.onclick(show_lobby)

		# 키보드모드
		# 키보드의 space 키를 누르면 이벤트 발생으로 lobby 보여주는 함수 호출
		screen.onkeyrelease(show_lobby, "space")

	def draw_init():
		"""
		draw_init 함수에 대한 설명
		: 초기 화면 관련 그리는 것에 대한 함수
		"""
		global pen
		# 이전에 그린 것들 전부 다 지우기
		pen.clear() 

		# 현재 cursor가 보인다면 숨기기
		if pen.isvisible():
			pen.ht()

		# 펜 들고 위치 이동 및 필요한 텍스트 작성
		pen.up()
		pen.goto(0,100)
		pen.write("거북이 선물받기", align='center', font=("", 30))

		# 펜 들고 위치 이동 및 필요한 텍스트 작성
		pen.goto(0,-100)
		pen.write("키보드로 시작하려면 space키 누르고, 마우스로 시작하려면 클릭을 해주세요",align='center', font=("", 10))
	
	"""
	show_init 함수에 대한 설명
	: 초기화면 관련 함수 호출을 통해 초기화면을 보여주는 함수
		초기화면에서는 keyboard 입력 타입과 mouse 입력 타입을 구분해서 받을 수 있도록
		사용자에게 안내하고 입력에 따라 모드 변경을 실시한다.
	"""
	# 함수호출
	set_init_handler()
	draw_init()


def show_lobby(*args):
	def set_lobby_handler():
		"""
		set_lobby_handler 함수에 대한 설명
		: lobby 화면 관련 이벤트 처리에 대한 정의를 하는 함수
		"""
		global screen
		global config
		# 모드에 따라서 필요한 이벤트 처리 함수 정의
		if config['mode'] == 'mouse':
			# 마우스 모드에서는 키 입력에 대한 이벤트 삭제
			screen.onkeyrelease(None, "space")

			# 클릭에 대한 이벤트를 수정한다
			# 원래는 클릭하면 show_lobby 함수 호출 
			# -> show_game 함수 호출로 변경
			screen.onclick(show_game)

		elif config['mode'] == 'key':
			# 키보드모드에서는 클릭에 대한 이벤트 삭제
			screen.onclick(None)

			# 키 입력에 따른 이벤트 추가
			screen.onkeyrelease(None, "space")
			screen.onkeyrelease(show_game_a, "a")
			screen.onkeyrelease(show_game_s, "s")
			screen.onkeyrelease(show_game_d, "d")

	def draw_lobby():
		def __draw_button(pen,x,y,difficulty,button=None, hover=False):
			"""
			__draw_button 함수에 대한 설명
			: 실제로 값을 받아서 버튼을 그리는 함수로 함수 인자에 기본값을 주어서
				button 값이 들어올 때(키보드모드)는 관련 버튼 글자를 추가해서 그린다.
				hover가 True로 들어오면(마우스모드) 해당 버튼을 채우기와 글자 색 변경을 통해
				마우스가 올라오는 것을 반영해준다.
			"""
			global screen

			# 펜이 그리기 시작할 위치로 이동
			pen.goto(-200,y+30)
			# 마우스가 버튼 위로 올라왔다면, hover = True
			if hover :
				# 채우기 시작
				pen.begin_fill()
			# 그리기 위해서 펜 내리기
			pen.down()
			# 사각형 그리기
			pen.goto(200,y+30)
			pen.goto(200,y)
			pen.goto(-200,y)
			pen.goto(-200,y+30)
			# 채우기 중이면 채우기 끝
			if hover :
				pen.end_fill()
			# 펜 들기
			pen.up()
			# 글자 쓸 위치로 이동
			pen.goto(x,y)
			# 채우기 했으면 글자색 바꿔주기
			if hover :
				pen.color('white')
			# 글자 쓰기
			pen.write(f"{difficulty}{'' if config['mode']=='mouse' else f'(button {button})'}",align='center', font=("", 20))
			pen.color('black')

		def draw_button(e):
			"""
			draw_button 함수에 대한 설명
			: 마우스가 움직일 때마다 호출용으로 만든 함수로 상황에 따라 적절한 인자를
				__draw_buttn 함수에 넣어서 적절하게 버튼을 그리도록 유도한다.
			"""
			global is_first
			global is_hover
			global button_pens

			# 첫번째 그리는 거라면, 아직 버튼이 없기 때문에 바로 버튼을 그린다.
			if is_first:
				# 다음부터는 여기로 안 들어오게 False처리
				is_first = False
				
				# 버튼 그리기
				__draw_button(button_pens[0]['pen'],0,-10,'EASY','A')
				__draw_button(button_pens[1]['pen'],0,-60,'NORMAL','S')
				__draw_button(button_pens[2]['pen'],0,-110,'HARD','D')

			# 이미 한번 그린 상태에서 다시 호출됐을 때
			else :
				# 마우스의 위치가 버튼 안쪽인지 확인
				if 50<=e.x<=450 :
					# easy 버튼 안쪽인 경우
					if 230<e.y<260:
						# 아직 hover 처리가 안되어 있다면
						if not is_hover:
							# hover처리할꺼니까 True로 바꿔주기
							is_hover = True
							# 첫번쨰 pen(easy button 그린 녀석)에 값도 변경
							button_pens[0]['hover'] = True
							# 첫번째 pen으로 그린 거 다 지우고
							button_pens[0]['pen'].clear()
							# 첫번쨰 pen으로 hover 상태로 다시 그리기
							__draw_button(button_pens[0]['pen'],0,-10,'EASY','A',True)

					elif 280<e.y<310 :
						# easy 버튼이랑 알고리즘 동일
						if not is_hover: 
							is_hover = True
							button_pens[1]['hover'] = True
							button_pens[1]['pen'].clear()
							__draw_button(button_pens[1]['pen'],0,-60,'NORMAL','S',True)

					elif 330<e.y<360 :
						# easy 버튼이랑 알고리즘 동일
						if not is_hover:
							is_hover = True
							button_pens[2]['hover'] = True
							button_pens[2]['pen'].clear()
							__draw_button(button_pens[2]['pen'],0,-110,'HARD','D',True)

					# 버튼 밖으로 마우스가 나왔을 때
					else :
						# hover로 처리된 버튼이 있는 경우
						if is_hover:
							# hover False로 변경
							is_hover = False
							# 돌면서 실제로 hover 그린 놈 찾기
							for i in range(3):
								# 이 펜이 hover를 그렸다면
								if button_pens[i]['hover']:
									# 이 펜이 그린거 다 지우고
									button_pens[i]['pen'].clear()
									# hover False로 바꿔주고
									button_pens[i]['hover'] = False
									# 그 펜에 맞게 버튼 그리기
									if i == 0 :
										__draw_button(button_pens[i]['pen'],0,-10,'EASY','A')
									elif i == 1:
										__draw_button(button_pens[i]['pen'],0,-60,'NORMAL','S')
									elif i == 2:
										__draw_button(button_pens[i]['pen'],0,-110,'HARD','D')
				else:
					# 이것도 버튼 밖에 벗어난 경우 알고리즘 동일
					if is_hover:
						is_hover = False
						for i, button_pen in enumerate(button_pens):
							if button_pen['hover']:
								button_pen['hover'] = False
								button_pen['pen'].clear()
								if i == 0 :
									__draw_button(button_pen['pen'],0,-10,'EASY','A')
								elif i == 1:
									__draw_button(button_pen['pen'],0,-60,'NORMAL','S')
								elif i == 2:
									__draw_button(button_pen['pen'],0,-110,'HARD','D')
		
		"""
		draw_lobby 함수에 대한 설명
		: 로비 화면 관련 그리는 것에 대한 함수
		"""
		global screen
		global pen
		global config
		global is_first
		global is_hover
		global button_pens
		global user_name

		# 사용자의 이름 입력 받기!
		user_name = screen.textinput('거북이 선물받기 이름 입력창','이름을 입력해주세요 : ')

		# 이전에 그린 것들 전부 다 지우기
		pen.clear() 

		# 현재 cursor가 보인다면 숨기기
		if pen.isvisible():
			pen.ht()
		# pen 들고 이동해서 텍스트 작성하기
		pen.up()
		pen.goto(0,130)
		pen.write(f"{user_name}님",align='center', font=("", 20))
		pen.goto(0,100)
		pen.write("원하는 난이도를 선택해주세요",align='center', font=("", 20))

		# 마우스 모드에는 button들을 마우스가 올라오면 색상이 변하게 하기 위해서
		# 별도의 펜을 생성해서 그림.
		if config['mode'] == 'mouse':
			# 펜 3개를 만들고 리스트에 추가
			button_pens = [{'pen':t.Turtle(),'hover':False} for _ in range(3)]
			# for문으로 펜 하나씩 꺼내서 초기 셋팅해주기
			for button_pen in button_pens:
				button_pen['pen'].ht()
				button_pen['pen'].up()
				button_pen['pen'].speed(0)
			
			# 버튼을 그리기 위한 필요한 boolean 변수 선언
			is_first = True
			is_hover = False

			# 마우스 움직임에 따른 버튼 그리기 함수 연결
			screen.cv.master.bind('<Motion>', draw_button)

		elif config['mode'] == 'key':
			# 키보드 모드는 키 입력을 통해서 연결될 수 있도록 버튼 그려주기
			# 마우스가 올라오는 이벤트는 없으므로 그냥 펜으로 바로 그리기 
			__draw_button(pen,0,-10,'EASY','A')
			__draw_button(pen,0,-60,'NORMAL','S')
			__draw_button(pen,0,-110,'HARD','D')

	
	"""
	show_lobby 함수에 대한 설명
	: 로비화면 관련 함수 호출을 통해 로비화면을 보여주는 함수
		구분된 입력모드에 따른 버튼 구현과 그에 따른 이벤트 처리 준비
	"""
	global config
	global screen
	# 모드 설정
	# 클릭이벤트로 함수를 호출하면 args에 마우스가 클릭할 때 x,y 좌표가 들어가지만
	# 버튼클릭이벤트로 함수를 호출하면 아무것도 안 들어가있다.
	# 숫자의 경우 0이 아니면 True 처리가 되기 때문에
	# 길이를 확인해서 길이가 True이면 mouse, False이면 key로 설정한다.
	config['mode'] = 'mouse' if len(args) else 'key'
	set_lobby_handler()
	draw_lobby()
	screen.listen()

# 키보드모드 관련 함수
# a버튼 누르기(easy 모드)
def show_game_a():
	# 버튼 위치값을 바로 부여해서 show_game 함수 호출하기
	show_game(0,0)

# s버튼 누르기(normal 모드)
def show_game_s():
	# 버튼 위치값을 바로 부여해서 show_game 함수 호출하기
	show_game(0,-50)
	
# d버튼 누르기(hard 모드)
def show_game_d():
	# 버튼 위치값을 바로 부여해서 show_game 함수 호출하기
	show_game(0,-100)

def show_game(*args):	
	"""
	show_game 함수에 대한 설명
	: 실제 게임 화면에 대한 화면 및 기타 모든 처리 함수에 대해서 
		적절한 순서로 호출하여 처리하는 함수
	"""
	global screen
	global user_name
	global config
	global pen
	global button_pens

	# 클릭 시 클릭된 위치에 따라서 난이도 조절
	# 버튼 입력 시에도 클릭하는 것과 같은 위치로 입력되도록 함(code 281~295 lines)
	x,y = args[0],args[1]
	if -200<=x<=200 :
		if -10<=y<20:
			config['difficulty']='easy'
		elif -60<y<-30 :
			config['difficulty']='normal'
		elif -110<y<-80 :
			config['difficulty']='hard'
		# 이상한 위치 클릭하면 아무것도 처리 안하기
		else :
			return None
	# 이상한 위치 클릭하면 아무것도 처리 안하기
	else :
		return None

	# 로비 화면 지우기
	pen.clear()
	# 마우스 모드라면
	if config['mode']=='mouse':
		# 연결된 이벤트 삭제하고
		screen.cv.master.bind('<Motion>', lambda e: e)
		screen.onclick(None)

		# 따로 그린 버튼도 삭제해주기
		for button_pen in button_pens:
			button_pen['pen'].clear()
			button_pen['pen'].reset()
			button_pen['pen'].ht()

	# 게임 진행시에 필요한 값을 미리 초기화하기
	# 난이도에 따라 값 설정 변경
	global rmv,umv,omv,score,life,objects
	rmv = 5 if config['difficulty']=='easy' else 6 if config['difficulty']=='normal' else 8
	umv = 10 if config['difficulty']!='hard' else 12
	omv = 10 if config['difficulty']!='hard' else 15
	score = 0
	life = 3 if config['difficulty']=='easy' else 2 if config['difficulty']=='normal' else 1

	# 선물이나 장애물 생성시에 담아서 관리할 list 생성
	objects =[]

	# 펜 숨기고
	if pen.isvisible():
		pen.ht()
	# 펜 들고 위치 이동해서 좌측 상단에 정보 텍스트 쓰기
	pen.up()
	pen.goto(-240,230)
	pen.write(f"게임모드 : {'마우스' if config['mode']=='mouse' else '키보드'}",align='left', font=("", 10))
	pen.goto(-240,215)
	pen.write(f"게임 난이도 : {'쉬움' if config['difficulty']=='easy' else '보통' if config['difficulty']=='normal' else '어려움'}",align='left', font=("", 10))
	pen.goto(-240,200)
	pen.write(f"사용자 : {user_name}님",align='left', font=("", 10))
	pen.goto(-240,185)
	pen.write("현재 점수 :",align='left', font=("", 10))
	pen.goto(-240,170)
	pen.write("현재 체력 :",align='left', font=("", 10))

	global score_pen, life_pen, user_pen
	# 점수랑 체력은 게임 중간중간 수정하기 위해서 따로 펜 만들어서 그리기
	# 점수 펜 생성 및 초기화하고 점수 쓰기
	score_pen = t.Turtle()
	score_pen.ht()
	score_pen.up()
	score_pen.speed(0)
	score_pen.goto(-165,185)
	score_pen.write(f"{score}점",align='left', font=("", 10))
	
	# 체력 펜 생성 및 초기화하고 체력 쓰기
	life_pen = t.Turtle()
	life_pen.ht()
	life_pen.up()
	life_pen.speed(0)
	life_pen.goto(-165,170)
	life_pen.write(f"{'O'*life}",align='left', font=("", 10))

	# user가 조정하는 거북이도 중간중간 변경이 필요해서 따로 그리기
	user_pen = t.Turtle()
	user_pen.ht()
	user_pen.shape('turtle')
	user_pen.shapesize(2,2)
	user_pen.fillcolor('black')
	user_pen.speed(0)
	user_pen.up()
	user_pen.goto(0,-150)
	user_pen.left(90)
	user_pen.st()
	user_pen.speed(1)

	# 마우스모드
	# 마우스 클릭 시에 마우스 위치로 설정하는 함수
	def draw_user(x,y):
		global user_x
		user_x=x

	# 키보드모드
	# 키보드 a 버튼을 누르면 왼쪽 끝단 위치로 설정
	def left_user():
		global user_x
		user_x = -220
		
	# 키보드 d 버튼을 누르면 오른쪽 끝단 위치로 설정
	def right_user():
		global user_x
		user_x = 220

	# 키보드 s 버튼을 누르면 거북이의 현재 위치로 설정
	def stop_user():
		global user_x, user_pen
		user_x = user_pen.xcor()


	# 위에서 정의한 함수들 모드에 맞게 연결하기
	global user_x
	user_x=0
	# 마우스 모드
	if config['mode']=='mouse':
		# 클릭 이벤트에 연결
		screen.onclick(draw_user)

	# 키보드 모드
	else:
		# 키 입력 이벤트에 연결
		screen.onkeyrelease(left_user, "a")
		screen.onkeyrelease(stop_user, "s")
		screen.onkeyrelease(right_user, "d")
		screen.listen()


	# 선물 주는 루돌프도 별도로 그리기
	rudolf = t.Turtle()
	rudolf.ht()
	rudolf.shape('turtle')
	rudolf.shapesize(2,2)
	rudolf.fillcolor('green')
	rudolf.speed(0)
	rudolf.up()
	rudolf.goto(-210,100)
	rudolf.speed(2)
	rudolf.right(90)
	rudolf.st()

	# life가 0이 되면 호출되면 엔딩 화면용 함수
	def show_ending():
		# 펜들 전부다 지우기, 안보이게 하기
		pen.clear()
		score_pen.clear()
		life_pen.clear()
		user_pen.ht()
		rudolf.ht()
		for obj in objects:
			obj.ht()

		# 펜 하나만 위치 이동해서 텍스트 쓰기
		pen.goto(0,0)
		pen.write("GAME OVER",align='center', font=("", 30))
		pen.goto(0,-40)
		pen.write(f"{user_name}님의 최종점수는 {score}점입니다.",align='center', font=("", 10))

	# 화면에 점수 업데이트하기
	def update_score():
		global score_pen
		score_pen.clear()
		score_pen.write(f"{score}점",align='left', font=("", 10))

	# 화면에 체력 업데이트하기
	def update_life():
		global life_pen
		life_pen.clear()
		life_pen.write(f"{'O'*life}",align='left', font=("", 10))
		# 체력 0 이하로 되면 엔딩 호출
		if life <= 0 :
			show_ending()
			screen.ontimer(screen.exitonclick, 3000)

	# 선물 혹은 장애물 만들기
	def make_object():
		def __make_object(pos,is_gift=True):
			# 성격에 맞는 형태로 turtle 만들기
			gift = t.Turtle()
			gift.ht()
			gift.shape(f"{'circle' if is_gift else 'triangle'}")
			gift.shapesize(1,1)
			gift.fillcolor(f"{'yellow' if is_gift else 'red'}")
			gift.speed(0)
			gift.up()
			gift.setposition(pos[0],pos[1])
			gift.st()
			return gift

		global objects
		# 선물이 나올 확률 조정
		# easy, normal mode는 0,1로 1대1 비율
		# hard 모드는 0,1,2 3개로 선물 1 : 2 장애물 비율로 선물 확률 하향
		is_gift = randint(0,1 if config['difficulty'] != 'hard' else 2)

		# 성격에 맞는 turtle 만들기 함수 호출
		if is_gift:
			objects.append(__make_object(rudolf.position()))
		else :
			objects.append(__make_object(rudolf.position(),False))

	# 화면에 선물 혹은 장애물 위치 업데이트
	def update_objects_position():
		global objects, user_pen, score, life
		# list 담아 놓은 거 for문으로 꺼내면서 확인
		for obj in objects:
			# y값 정해진 셋팅값만큼 빼서 밑으로 이동시키기
			obj.sety(obj.ycor()-omv)

			# user 거북이랑 부딪힐 수 있는 위치이면서 동시에 아직 보인다면(아직 user랑 부딪히지 않음)
			if -145 >= obj.ycor() and obj.isvisible():
				# 유저랑 위치 차이가 10 이하라면
				if abs(obj.xcor() - user_pen.xcor()) <= 10:
					# 오브젝트 숨기고
					obj.ht()
					# 오브젝트 성격에 따라 점수 올리거나 체력 내리기
					if obj.shape() == 'circle':
						score += 10
					else :
						life -= 1
			# 오브젝트 위치가 너무 내려가면 (user랑 안 부딪힘) 숨기기
			if obj.ycor() < -160 and obj.isvisible():
				obj.ht()

	# 화면에 선물주는 루돌프 위치 업데이트
	def update_rudolf_position():
		# 왼쪽 끝이나 오른쪽 끝으로 가면 방향 전화
		global rmv
		if rudolf.xcor() <= -220:
			rmv *= -1
		elif 220 <= rudolf.xcor():
			rmv *= -1
		# 방향에 맞게 셋팅값만큼 이동하기
		rudolf.setx(rudolf.xcor()+rmv)

	# 화면에 user 위치 업데이트
	def update_user_position():
		# user가 가고 싶어하는 위치랑 현재 위치의 차이를 구해서
		# 그에 맞게 방향 전환 시켜주기
		global user_x, umv
		if user_pen.xcor() < user_x :
			if umv < 0 :
				umv *= -1
		elif user_pen.xcor() > user_x :
			if umv > 0 :
				umv *= -1
		# 셋팅된 방향으로 셋팅값만큼 이동
		user_pen.setx(user_pen.xcor()+umv)

	# 일정 주기마다 업데이트 함수 호출해주는 함수
	def frame():
		update_rudolf_position()
		update_user_position()
		if not bool(randint(0,10)):
			make_object()
		update_objects_position()
		update_score()
		update_life()
		screen.ontimer(frame, 30)

	frame()


def main():
	# 실제로 호출 되는 메인함수
	global screen
	global pen
	global config

	# 화면 기본값 세팅
	screen = t.Screen()
	# 화면 크기
	screen.setup(width=500,height=500)
	# 화면 배경색
	screen.bgcolor(1,0.85,0.85)
	# 화면 제목
	screen.title("거북이 선물받기")

	# 메인 펜 생성
	pen = t.Turtle()
	pen.speed(0)

	# 설정값 초기화
	config = {
		"mode" : 'None',
		'difficulty' : 'easy'
	}

	# 초기화면 보이기 호출
	screen.listen()
	show_init()
	# 화면 안 꺼지게 유지해주는 함수
	TK.mainloop()


if __name__ == '__main__':
	# 메인 함수 호출
	main()