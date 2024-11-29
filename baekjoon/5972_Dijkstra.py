import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = int(1e8)

graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1)
visited = [False] * (V+1)

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w)) # u에서 v로 가는 가중치 w

def Dijkstra(start):
  q = []
  dist[start] = 0
  heapq.heappush(q, (dist[start], start)) # 우선순위(거리), 값(idx)

  while q:
    min_dist, min_idx = heapq.heappop(q)

    # if dist[min_idx] < min_dist:  # 이미 방문한 애
    #   continue

    if visited[min_idx]:
      continue
    visited[min_idx] = True

    for i in graph[min_idx]:
      dist[i[0]] = min(min_dist + i[1], dist[i[0]])
      heapq.heappush(q, (min_dist + i[1], i[0]))

Dijkstra(K)

for i in range(1, len(dist)):
  if dist[i] == INF:
    print("INF")
    continue
  print(dist[i])



# V, E = map(int, input().split())
# K = int(input())
# INF = int(1e8)

# graph = [[] for _ in range(V+1)]
# visited = [False]*(V+1)
# dist = [INF]*(V+1)

# for _ in range(E):
#   u, v, w = map(int, input().split())
#   graph[u].append([v, w]) # u에서 v로 가는 가중치 w

# def Shortest():
#   min_idx = 0
#   min_val = INF

#   for i in range(1, V+1):
#     if dist[i] < min_val and visited[i] == False:
#       min_idx = i
#       min_val = dist[i]
#   return min_idx

# def Dijkstra(start):
#   dist[start] = 0
#   visited[start] = True

#   for i in graph[start]:
#     dist[i[0]] = i[1]

#   for _ in range(V-1): 
#     min_idx = Shortest()
#     visited[min_idx] = True
#     for i in graph[min_idx]:
#       dist[i[0]] = min(dist[i[0]], dist[min_idx] + i[1])

# Dijkstra(K)

# for i in range(1, len(dist)):
#   if dist[i] == INF:
#     print("INF")
#     continue
#   print(dist[i])