# https://www.acmicpc.net/problem/1912

n = int(input())
num = list(map(int,input().split()))
dp = [0]
dp.extend(num)
maxValue = max(num)

for i in range(2,n+1):
    dp[i] += dp[i-1] if dp[i-1] > 0 else 0
    maxValue = max(maxValue, dp[i])
print(maxValue)

