# https://www.acmicpc.net/problem/1699

def isSquare(n):
    return int(n ** 0.5) ** 2 == n
n = int(input())
if isSquare(n):
    print(1)
else :
    dp = [1]*100001
    dp[2] = 2
    SqareNumber = []
    for i in range(3,n+1):
        if isSquare(i):
            SqareNumber.append(i)
            continue
        minValue = dp[1]+dp[i-1]
        for j in SqareNumber:
            minValue = min(minValue, dp[j]+dp[i-j])
        dp[i] = minValue
    print(dp[n])