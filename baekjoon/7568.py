n = int(input())
data = []
ans = []
for _ in range(n):
  x, y = map(int, input().split())
  data.append((x, y))

for i in range(n):
  rank = 1
  for j in range(n):
    if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
      rank += 1
  ans.append(rank)

for i in ans:
  print(i, end=" ")