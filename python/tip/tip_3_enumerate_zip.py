# Enumerate
# list의 index와 value를 unpacking
for i, v in enumerate(['zero','one','two']):
	print(i, v)
# 0 zero
# 1 one
# 2 two

dic = {i:v for i, v in enumerate('나는 착한 선배입니다.'.split())}
print(dic)
# {0: '나는', 1: '착한', 2: '선배입니다.'}

# # --------------------------------------------------

# zip
# 여러 list의 값들을 병렬적 묶어 tuple로 반환
alist = 'a1 a2 a3'.split()
blist = 'b1 b2 b3'.split()
for l in zip(alist, blist): 
	print(l)
# ('a1', 'b1')
# ('a2', 'b2')
# ('a3', 'b3')
for a, b in zip(alist, blist): 
	print(a,b)
# a1 b1
# a2 b2
# a3 b3

print([sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))])
# [111,222,333]