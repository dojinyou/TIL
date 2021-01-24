# https://www.acmicpc.net/problem/9465

for _ in range(int(input())):
    n = int(input())
    score = [list(map(int,input().split())) for _ in range(2)]

    dp = [[0]*3 for _ in range(n+1)]
    dp[1][0] = 0
    dp[1][1] = score[0][0]
    dp[1][2] = score[1][0]
    for i in range(2,n+1):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
        dp[i][1] = max(dp[i-1][0],dp[i-1][2])+score[0][i-1]
        dp[i][2] = max(dp[i-1][0],dp[i-1][1])+score[1][i-1]
    print(max(dp[n]))

