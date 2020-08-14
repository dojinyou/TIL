# list comprehenssions
# 기존의 list를 사용하여 간단히 다른 list를 만드는 기법
# list 포괄적인 표현
# 파이썬에서 가장 많이 사용하는 기법
# for loop + append보다 빠름.

# for loop + append 사용
result = []
for i in range(5):
  result.append(i)
print(result)
# [0, 1, 2, 3, 4]
# list Comprehenssion
result = [i for i in range(5)]
print(result)
# [0, 1, 2, 3, 4]

# list Comprehenssion
result = [i*2 for i in range(5)]
print(result)
# [0, 2, 4, 6, 8]

# Nested for loop
result = [i+j for i in range(5) for j in range(5)]
print(result)
# [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8]

# if문 사용
result = [i for i in range(10) if i % 2 == 0]
print(result)
# [0, 2, 4, 6, 8]

# quiz
result = [i+j for i in range(10) if i % 2 == 0 for j in range(2)]
print(result)