# https://www.acmicpc.net/problem/2133

n = int(input())
if bool(n%2):
    print(0)
else :
    dp = [0]*(n+1)
    dp[2] = 3

    for i in range(4,n+1,2):
        dp[i] = 2+2*sum(dp)+dp[i-2]
    print(dp[n])