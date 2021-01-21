# https://www.acmicpc.net/problem/9095

def plusCount(n):
    dp = [0]*11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4,n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]
    
n = int(input())

for _ in range(n):
    inputNum = int(input())
    print(plusCount(inputNum))
	



