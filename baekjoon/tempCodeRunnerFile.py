N = int(input())
A = [0] + list(map(int, input().split()))
dp = [1 for _ in range(N+1)]

for i in range(2, N+1):
  if A[i-1] < A[i]:
    dp[i] = dp[i-1] + 1
  else:
    dp[i] = dp[i-1] 

print(dp[-1])