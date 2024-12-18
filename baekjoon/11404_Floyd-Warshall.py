import sys

input = sys.stdin.readline
INF = int(1e8)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]
  
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b]) # 기본 : graph[a][b] = c

for i in range(1, n+1):
  for j in range(1, n+1):
    for k in range(1, n+1):
      graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print(0, end=' ')
    else:
      print(graph[a][b], end=' ')
  print()