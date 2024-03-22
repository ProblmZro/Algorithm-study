N = int(input())
stair = [0] + [int(input()) for _ in range(N)]
dp = [0 for _ in range(N+1)]

dp[1] = stair[1]
if N >= 2:
  dp[2] = stair[1] + stair[2]
if N >= 3:
  for i in range(3, N+1):
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[N])