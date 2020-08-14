# Collections module
# list, Tuple, Dictionary에 대한 built-in extend data structure modul
# 편의성, 효율 등을 제공

# deque(가변인자)
# stack과 queue를 모두 가능. list의 앞, 뒤로 입출력 가능
# list에 비해 효율적인 자료 저장 방식
from collections import deque
deque_list = deque()
for i in range(5):
	deque_list.append(i)
	deque_list.appendleft(i)
print(deque_list)
print(dir(deque_list))

# --------------------------------------------------------

# Counter
# 말 그대로 갯수를 세어주는 자료 구조
from collections import Counter
print(Counter("Hello world"))
# Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(Counter("Hello world").most_common(1))
# [('l', 3)]
print(*Counter("Hello world").most_common(1))
# ('l', 3)
# --------------------------------------------------------

# OrderDict
# 순서가 있는  dictionary
from collections import OrderedDict
d = {}
d['x']=100
d['y']=200
d['z']=300
d['l']=500
for i,v in d.items():
	print(i, v)

d = OrderedDict()
d['x']=100
d['y']=200
d['z']=300
d['l']=500
for i,v in d.items():
	print(i, v)

# --------------------------------------------------------

# defaultDict
# default 값이 있는  dictionary
from collections import defaultdict
d = defaultdict(lambda :0)
print(d['first'])