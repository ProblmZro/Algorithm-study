from sys import stdin
input = stdin.readline
INF = int(1e9)

def b_f(start):
  dist[start] = 0
  for i in range(N):
    for cur, next, cost in edges:
      if dist[cur] != INF and dist[next] > dist[cur] + cost:
        dist[next] = dist[cur] + cost
        if i == N - 1:
          return True
  return False

N, M = map(int, input().split())
edges = []
dist = [INF] * (N+1)

for _ in range(M):
  A, B, C = map(int, input().split())
  edges.append((A, B, C))

if b_f(1):
  print(-1)
else:
  for i in range(2, N+1):
    if dist[i] == INF:
      print(-1)
    else:
      print(dist[i])