import numpy as np

# make array 
np.array([1,2,3,4,5])
# array([1,2,3,4,5])

np.array([3,1.4,2,3,4])
# array([3.,1.4,2.,3.,4.])
# float type이 1개라도 있으면 전부 다 float tyep으로 변경

np.array([[1,2],
					[3,4]])
# 2차원 array도 가능

np.array([1,2,3,4], dtype='float')
# array([1.,2.,3.,4.])
# 데이터 타입을 명시할 경우 맞게 변환 시켜줌.

# array dtype
# python의 list와 다르게 1개의 데이터 타입을 사용할 수 있음.

arr = np.array([1,2,3,4], dtype=float)
print(arr)
print(arr.dtype)
print(arr.astype(int))

# 다양한 배열 만들기
np.zeros(10, dtype=int)
# array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

np.ones((3,5), dtype=float)
# array([[1., 1., 1., 1., 1.],
			# [1., 1., 1., 1., 1.],
			# [1., 1., 1., 1., 1.]])

np.arange(0, 10, 2)
# array([0, 2, 4, 6, 8])
# python의 range 함수랑 비슷하다.

np.linspace(0, 1, 5)
# array([0., 0.25, 0.5, 0.75, 1.])
# 첫번째 parameter에서 두번째 parameter까지 세번째parameter로 등분한다.

# 난수 생성
np.random.random([2,2])
# array[[0.30986539, 0.858663508],
# 			[0.89151021, 0.19304196]]

# 정규분포로 난수 생성
# 평균, 표준편차, shape
print(np.random.normal(0,1,(2,2)))
# array([[0.40905392 2.33743489],
# 			[2.68875695 0.76426522]])

# 정수 난수 생성
# 최소값, 최대값, shape
print(np.random.randint(0,10,(2,2)))
#array([[3 2],
# 			[7 5]]

print("1차원 array")
array = np.arange(10)
print(array)

# Q1. array의 자료형을 출력해보세요.
print(type(array))

# Q2. array의 차원을 출력해보세요.
print(array.ndim)

# Q3. array의 모양을 출력해보세요.
print(array.shape)

# Q4. array의 크기를 출력해보세요.
print(array.size)

# Q5. array의 dtype(data type)을 출력해보세요.
print(array.dtype)

# Q6. array의 인덱스 5의 요소를 출력해보세요.
print(array[5])

# Q7. array의 인덱스 3의 요소부터 인덱스 5 요소까지 출력해보세요.
print(array[3:6])

print("2차원 array")
matrix = np.arange(1, 16).reshape(3,5)  #1부터 15까지 들어있는 (3,5)짜리 배열을 만듭니다.
print(matrix)


# Q1. matrix의 자료형을 출력해보세요.
print(type(matrix))

# Q2. matrix의 차원을 출력해보세요.
print(matrix.ndim)

# Q3. matrix의 모양을 출력해보세요.
print(matrix.shape)

# Q4. matrix의 크기를 출력해보세요.
print(matrix.size)

# Q5. matrix의 dtype(data type)을 출력해보세요.
print(matrix.dtype)

# Q6. matrix의 (2,3) 인덱스의 요소를 출력해보세요.
print(matrix[2][3])

# Q7. matrix의 행은 인덱스 0부터 인덱스 1까지, 열은 인덱스 1부터 인덱스 3까지 출력해보세요.
print(matrix[:2,1:4])

