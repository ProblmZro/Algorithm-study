N = int(input())

def DP(N):
  if N==1:
    return 3
  dp = [1] * (N+1)
  dp[1], dp[2] = 3, 7
  for i in range(3, N+1):
    dp[i] = (2 * dp[i-1] + dp[i-2]) % 9901
  return dp[N]

print(DP(N))