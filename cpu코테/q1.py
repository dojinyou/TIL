import sys
input = sys.stdin.readline
n, V = map(int, input().split())
item_dict = {}
for i in range(n):
    v, p = map(int, input().split())
    if item_dict.get(v):
        item_dict[v] = max(p, item_dict.get(v))
    else :
        item_dict[v] = p
for i in range(1, V+1):
    for vol, price in sorted(item_dict.items(), key=lambda v:v[0]):



# 예제 입력
# 5 30
# 5 10
# 15 20
# 3 8
# 10 10
# 9 4