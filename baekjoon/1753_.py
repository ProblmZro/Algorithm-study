import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
INF = int(1e9)

K = int(input())

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w)) # u -> v (가중치 w)

def dijkstra(start, graph, n):
  distance = [INF] * (n+1)
  q = []
  heapq.heappush(q, (0, start)) # (거리, 노드)
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:  # 이미 방문했다면
      continue
    for next_node, cost in graph[now]:
      new_dist = dist + cost
      if new_dist < distance[next_node]:  # 직접 연결보다 짧으면
          distance[next_node] = new_dist
          heapq.heappush(q, (new_dist, next_node))

  return distance

res = dijkstra(K, graph, V)

for i in range(1, len(res)):
  if res[i] >= 1e9:
    print("INF")
  else : print(res[i])