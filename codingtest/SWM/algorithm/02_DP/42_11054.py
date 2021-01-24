# https://www.acmicpc.net/problem/11054

n = int(input())
num = list(map(int,input().split()))
dp = [[1,1] for _ in range(n+1)]
maxValue = 1
for i in range(2,n+1):
    for j in range(1,i):
        if (num[j-1] < num[i-1]) and (dp[j][0]+1 > dp[i][0]) :
            dp[i][0] = dp[j][0]+1
        if (num[j-1] > num[i-1]) and (max(dp[j][0],dp[j][1])+1 > dp[i][1]) :
            dp[i][1] = max(dp[j][0],dp[j][1])+1
    maxValue = max(maxValue, dp[i][0], dp[i][1])
print(maxValue)

