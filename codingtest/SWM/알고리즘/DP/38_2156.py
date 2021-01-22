# https://www.acmicpc.net/problem/2156

n = int(input())
drink = [int(input()) for _ in range(n)]
dp = [[0]*2 for _ in range(n+1)]
dp[1][1] = drink[0]
for i in range(2,n+1):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = max(dp[i-1][0], dp[i-2][0]+drink[i-2])+drink[i-1]
print(max(dp[n]))

