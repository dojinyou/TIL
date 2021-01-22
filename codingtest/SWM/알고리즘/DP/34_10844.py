# https://www.acmicpc.net/problem/10844

n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(1,10):
    dp[1][i] = 1
for i in range(2,n+1):
    for j in range(10):
        if j == 0 :
            dp[i][j] = dp[i-1][j+1]
        elif j == 9 :
            dp[i][j] = dp[i-1][j-1]
        else :
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1]) % 1000000000
# dp[1] = 9  #0 1 1 1 1 1 1 1 1 1 / 1
# dp[2] = 17 #1 1 2 2 2 2 2 2 2 1 / 2
# dp[3] = 32 #1 3 3 4 4 4 4 4 3 2 / 3
# dp[4] = 61 #3 4 7 7 8 8 8 7 6 3 / 6
# dp[5] = 116#4 10 11 15 15 16 15 14 10 6 / 10
# dp[6] = 222#10 15 25 26 31 30 30 25 20 10 / 20
print(sum(dp[n])%1000000000)


