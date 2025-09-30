# 모든 노드 -> 다른 노드 최단 거리 : 플로이드-워셜
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c)) # a->b c비용

def floyd(n, graph):
  INF = int(1e9)
  dist = [[INF] * (n+1) for _ in range(n+1)]

  # 거리 초기화
  for a in range(1, n+1):
    dist[a][a] = 0  # 자기 자신
    for b, c in graph[a]:
      dist[a][b] = min(dist[a][b], c) # 간선 여러 개일 수 있어서

  for k in range(1, n + 1): # 경유 노드
    for a in range(1, n + 1): # 출발 노드
      for b in range(1, n + 1): # 도착 노드
        dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

  return dist

res = floyd(n, graph)

for i in range(1, len(res)):
  print(*[0 if x == int(1e9) else x for x in res[i][1:]])