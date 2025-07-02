N, M = map(int, input().split())
map = []

for _ in range(N):
  map.append(input())

min_l = min(N, M)
res = 0
for l in range(0, min_l): # l: 변 길이
  for i in range(0, N-l):
    for j in range(0, M-l):
      if map[i][j] == map[i+l][j] == map[i][j+l] == map[i+l][j+l]:
        res = l

res += 1
print(res*res)