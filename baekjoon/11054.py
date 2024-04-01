N = int(input())
A = list(map(int, input().split()))
dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]

for i in range(N):
  for j in range(0, i):
    if A[i] > A[j]:
      dp1[i] = max(dp1[j]+1,dp1[i])

for i in range(N-1, -1, -1):
  for j in range(N-1, i, -1):
    if A[i] > A[j]:
      dp2[i] = max(dp2[j]+1,dp2[i])

res = [0 for _ in range(N)]
for i in range(N):
  res[i] = dp1[i] + dp2[i]
print(max(res) - 1)

# 1 2 2 1 3 3 4 5 2 1
# 1 5 2 1 4 3 3 3 2 1