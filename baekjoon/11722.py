N = int(input())
A = [0] + list(map(int, input().split()))
dp = [1 for _ in range(N+1)]

for i in range(2, N+1):
  for j in range(1, i):
    if A[j] > A[i]:
      dp[i] = max(dp[j]+1, dp[i])

print(max(dp))