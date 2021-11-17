from collections import deque
n = 10 # 정점의 개수

# 그래프 표현 방식
# 1. 인접 행렬
matrix = [[0]*n for _ in range(n)] # 이중 배열 만들 때 많이 씀
# 2. 인접 연결리스트(리스트, 배열) 만들기
matrix = [[] for _ in range(n)]

# 입력 값을 받아서 매트릭트 채우기

def aDFS(v):
  visited[v] = True #global 변수
  for item in matrix[v]:
    if not visited[item] :
      aDFS(item)
visited = [False] * n

s = 0 # 시작 정점
visited[s] = True
for item in matrix[s]:
  if not visited[item]:
    aDFS(item)
    