N = int(input())
seq = list(map(int, input().split()))
dp = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]

for i in range(N-1):
  if seq[i] <= seq[i+1]:
    dp[i+1] = dp[i] + 1

for i in range(N-1):
  if seq[i] >= seq[i+1]:
    dp2[i+1] = dp2[i] + 1

print(max(max(dp),max(dp2)))