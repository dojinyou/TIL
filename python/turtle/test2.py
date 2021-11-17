from random import randint
from turtle import TurtleScreen,RawTurtle,TK
import turtle as t
	
rmv = 5
umv = 10
omv = 10
score = 0
life = 3
objects = []
screen = t.Screen()
user_name = '도진'
config = {
	"mode" : 'mouse',
	'difficulty' : 'easy'
}
pen = t.Turtle()
pen.clear()

# 왼쪽 상단에 이름과 점수 보여주기
if pen.isvisible():
	pen.ht()
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
# 점수는 수정하기 위해서 따로 펜 만들어서 그리기
score_pen = t.Turtle()
score_pen.ht()
score_pen.up()
score_pen.speed(0)
score_pen.goto(-165,185)
score_pen.write(f"{score}점",align='left', font=("", 10))
# life pen
life_pen = t.Turtle()
life_pen.ht()
life_pen.up()
life_pen.speed(0)
life_pen.goto(-165,170)
life_pen.write(f"{'O'*life}",align='left', font=("", 10))
# user turtle
def draw_user(x,y):
	global user_x
	user_x=x

user_x=0
user_y=0
global user_pen
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
screen.onclick(draw_user)


# 선물 주는 루돌프 역 turtle
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

def update_score():
	global score_pen
	score_pen.clear()
	score_pen.write(f"{score}점",align='left', font=("", 10))
def update_life():
	global life_pen
	life_pen.clear()
	life_pen.write(f"{'O'*life}",align='left', font=("", 10))
	if life == 0 :
		show_ending()
def r_make():
	def make_gift(pos,is_gift=True):
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
	is_gift = randint(0,1 if config['mode'] != 'hard' else 2)
	if is_gift:
		objects.append(make_gift(rudolf.position()))
	else :
		objects.append(make_gift(rudolf.position(),False))

def update_objects_position():
	global objects, user_pen, score, life
	for obj in objects:
		obj.sety(obj.ycor()-omv)
		if obj.ycor() == -150:
			print(obj.xcor(),user_pen.xcor())
			if abs(obj.xcor() - user_pen.xcor()) <= 10:
				if obj.shape() == 'circle':
					score += 10
				else :
					life -= 1
			obj.ht()

def update_rudolf_position():
	global rmv
	# print(rudolf.xcor())
	if rudolf.xcor() <= -220:
		print('방향바뀜1')
		rmv *= -1
	elif 220 <= rudolf.xcor():
		print('방향바뀜2')
		rmv *= -1
	rudolf.setx(rudolf.xcor()+rmv)

def update_user_position():
	global user_x, umv
	if user_pen.xcor() < user_x :
		if umv < 0 :
			umv *= -1
	elif user_pen.xcor() > user_x :
		if umv > 0 :
			umv *= -1
	user_pen.setx(user_pen.xcor()+umv)

def show_ending():
	pen.clear()
	user_pen.clear()
	score_pen.clear()
	life_pen.clear()
	rudolf.clear()
	for obj in objects:
		obj.clear()
	pen.goto(0,0)
	score_pen.write("GAME OVER",align='center', font=("", 30))
	pen.goto(0,-20)
	score_pen.write(f"{user_name}님의 최종점수는 {score}점입니다.",align='center', font=("", 10))

def frame():
	update_rudolf_position()
	update_user_position()
	if not bool(randint(0,10)):
		r_make()
	update_objects_position()
	update_life()
	update_score()
	screen.ontimer(frame, 10)

	
frame()
TK.mainloop()