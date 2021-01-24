# https://www.acmicpc.net/problem/11052

n = int(input())
price = [0]
price.extend(list(map(float,input().split())))
dp = [int(p) for p in price]

for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j])
print(dp[n])















# cost = 0
# priceRate = [p/i if i!=0 else 0.0 for i,p in enumerate(price)]
# print(f'priceRate = {priceRate}')
# cnt = 0
# while n != 0 :
#     maxIndex = 0
#     print(f'cnt={cnt}, n={n}')
#     for i in range(1,n+1):
#         print(f'i={i}, maxIndex={maxIndex}')
#         if priceRate[maxIndex] < priceRate[i] :
#             maxIndex = i
#         elif priceRate[maxIndex] == priceRate[i] and n % maxIndex > n % i:
#             maxIndex = i

#     print(f'maxIndex={maxIndex}')
#     count = n // maxIndex
#     cost += count * int(price[maxIndex])
#     n -= maxIndex * count
#     cnt += 1
#     if cnt > 20:
#         break
# print(cost)


