N = int(input())
a = [0] * N
for i in range(N):
  a[i] = list(map(int, input().split()))

for i in range(1, N):
  a[i][0] = min(a[i-1][1], a[i-1][2]) + a[i][0]
  a[i][1] = min(a[i-1][0], a[i-1][2]) + a[i][1]
  a[i][2] = min(a[i-1][0], a[i-1][1]) + a[i][2]

print(min(a[-1]))