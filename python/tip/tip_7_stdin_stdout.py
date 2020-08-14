# sys.stdin
# 표준입출력을 위한 장치 중 입력 통로로 input()보다 처리 속도가 빠르다.

import sys

# a = input()
# a = sys.stdin.readline()
# sys.stdout.write(a)
# print(a)

# --------------------------------------------------

# if else 한줄 쓰기
# for i in range(5):
# 	result = "짝수" if i % 2 == 0 else "홀수"
# 	print(result)

# --------------------------------------------------

# assert
# 가정설정문? test 및 debug에 도움을 준다.
x = int(input())
assert x % 2 == 0, "홀수입니다."
print(x)


# asyncio, await, decorator, wraps 등 다양한 것들에 대해서도 공부해보길!