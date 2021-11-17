import sys
matrix = [30,35,15,5,10,20,25]
n = len(matrix) #7
result = [[0]*(n) for _ in range(n)]


# 시작 index  : i (0 ~ n-3)
# 체인의 길이 : l (2 ~ n-1)
# 곱셈의 위치 : k (i+1 ~ i+j-1) 
# 시작 index보다 크고, 끝 index보다 작아야한다.
# 최소 곲셈   : 값

for l in range(2, n): # 체인의 길이를 늘려가면 문제 해결
  for i in range(n-l): # 시작 위치는 최대 길이에서 체인 길이를 뺀 값까지
    j = i+l # 행렬 곱 체인의 마지막 index 
    min_product = sys.maxsize # 최소값 초기화
    for k in range(i+1, j): # 중간 곱셈 위치 순회
      # 곱셈 수 구하기
      # result[i][k] = i시작 k끝일 때 최소 곱셈 수
      # result[k][j] = k시작 j끝일 때 최소 곱셈 수
      # matrix[i]*matrix[k]*matrix[j] : 그 두가지 행렬 곱셈 결과를 곱할 때 횟수
      cnt_product = result[i][k]+result[k][j]+matrix[i]*matrix[k]*matrix[j]
      # 최소 곱셈 수 갱신
      min_product = min(cnt_product,min_product)
    # 중간 위치 다 확인 후 최소값 할당
    result[i][j] = min_product
# 첫 값에서부터 마지막값까지의 최소곲 갑
print(result[0][n-1]) 
# 전체 확인.
[print(result[i]) for i in range(n)]