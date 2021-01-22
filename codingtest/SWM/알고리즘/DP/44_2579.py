# https://www.acmicpc.net/problem/2579

n = int(input())
num = [0]
for _ in range(n):
    num.append(int(input()))
dp = [[0,0] for _ in range(n+1)]
dp[1][1] = num[1]

for i in range(2,n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = max(dp[i-1][0], dp[i-2][0]+num[i-1])+num[i]
print(dp)
print(dp[n][1])