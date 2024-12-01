import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
INF = int(1e8)

graph = [[] for _ in range(N+1)]

for _ in range(M):
  start, end, t = map(int, input().split())
  graph[start].append((end, t))

def dijkstra(start):
  dist = [INF] * (N+1)
  visited = [False] * (N+1)
  
  q = []
  dist[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    cur_dist, cur_idx = heapq.heappop(q)

    if visited[cur_idx]:
      continue
    visited[cur_idx] = True
    
    for i in graph[cur_idx]:
      dist[i[0]] = min(dist[i[0]], cur_dist + i[1])
      heapq.heappush(q, (cur_dist + i[1], i[0]))

  return dist

res = dijkstra(X)
for i in range(N):
  res[i+1] += dijkstra(i+1)[X]

print(max(res[1:]))

# print(dijkstra(2))
# print(dijkstra(1)[2])
# print(dijkstra(3)[2])
# print(dijkstra(4)[2])


