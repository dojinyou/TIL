# https://www.acmicpc.net/problem/11057

n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        # print(f'i ={i}, j={j}, sum={sum(dp[i-1][:j+1])}')
        dp[i][j] = sum(dp[i-1][:j+1])%10007
print(sum(dp[n])%10007)

