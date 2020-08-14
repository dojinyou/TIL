# lambda(anonymous function)
# 익명함수
# python 3부터 권장하진 않으나 효율적인 코드 작성을 위해 종종 쓰임.
def f(x, y):
  return x + y
print(f(1, 4))
# 5
f = lambda x, y: x + y
print(f(1, 4))
# 5
print((lambda x: x + 1)(5))
# 6

# # --------------------------------------------------

# map
# sequence 자료형의 각 element들에 동일한 fuonction을 적용
ex = [1,2,3]
print(list(map(lambda x:x**2, ex)))
# [1, 4, 9]
print(list(map(lambda x,y:x+y, ex, ex)))
# [2, 4, 6]
print(list(map(lambda x:x**2 if x % 2 == 0 else x, ex)))
# [1, 4, 3]

# # --------------------------------------------------

# reduce
# sequence 자료형의 element를 순회하면서 함수를 적용
from functools import reduce
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))
# 15
print(reduce(lambda x,y:x+y,[1,2,3,4,5],-5))
# 10

def factorial(n):
	return reduce(
		lambda x,y: x*y, range(1,n+1))
print(factorial(3))
# 6 