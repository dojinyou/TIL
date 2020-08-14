# Asterisk(*)
# 단순 곱셈, 제곱연산, 가변 인자 등에서 다양하게 사용됨

# *args (가변인자)
# 인자가 몇개 들어올 지 모를 때 tuple type으로 인자를 받음
def asterisk_test1(a, *args):
	print(a, args)
	print(type(args))
asterisk_test1(1,2,3)
# 1 (2, 3)
# <class 'tuple'>

# --------------------------------------------------------

# **kargs (가변인자)
# 인자가 몇개 들어올 지 모를 때 keyward를 통해서 dictionary type으로 인자를 받음
def asterisk_test2(a, **kargs):
	print(a, kargs)
	print(type(kargs))
asterisk_test2(1,b=2,c=3)
# 1 {'b': 2, 'c': 3}
# <class 'dict'>

# --------------------------------------------------------

# unpacking
# sequence type으로 받은 인자를 unpacking 해줌
def asterisk_test3(a, args):
	print(a, *args)
	print(type(args))
asterisk_test3(1,(2,3))
asterisk_test3(1,[2,3])
# 1 2 3
# <class 'tuple'>

# --------------------------------------------------------

def asterisk_test4(a, *args):
	print(a, args)
	print(type(args))
asterisk_test4(1,(2,3))
# 1 ((2, 3),)
# <class 'tuple'>
asterisk_test4(1,*(2,3))
# 1 (2, 3)
# <class 'tuple'>

def asterisk_test5(a, b, c):
	print(a, b, c)
asterisk_test5(1,**{'b':2,'c':3})
# 1 2 3

for data in zip(*([1,2], [3,4], [5,6])):
	print(sum(data))