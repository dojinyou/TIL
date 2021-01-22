# https://www.acmicpc.net/problem/11055

n = int(input())
num = list(map(int,input().split()))
dp = [num[i-1] if i!=0 else 0 for i in range(n+1)]
for i in range(2,n+1):
    for j in range(1,i):
        if (num[j-1] < num[i-1]) and (dp[j]+num[i-1] > dp[i]) :
            dp[i] = dp[j]+num[i-1]
print(max(dp))

