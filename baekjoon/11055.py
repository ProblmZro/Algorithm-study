N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]

dp[0] = A[0]
for i in range(1, N):
  # isNone = True
  for j in range(0, i):
    if A[j] < A[i]:
      dp[i] = max(dp[j]+A[i], dp[i])
      # isNone = False
    else:
      dp[i] = max(dp[i], A[i])
  # if isNone :
  #   dp[i] = A[i]

print(max(dp))