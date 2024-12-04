from sys import stdin
input = stdin.readline
INF = int(1e9)

def b_f():
  for i in range(N):
    for cur, next, cost in edges:
      if dist[next] > dist[cur] + cost:
        dist[next] = dist[cur] + cost
        if i == N - 1:
          return True
  return False

for _ in range(int(input())):
  N, M, W = map(int, input().split())
  edges = []
  dist = [INF] * (N+1)
  
  for _ in range(M):
    S, E, T = map(int, input().split())
    edges.append((S, E, T))
    edges.append((E, S, T))
  for _ in range(W):
    S, E, T = map(int, input().split())
    edges.append((S, E, -T))

  if b_f():
    print("YES")
  else:
    print("NO")