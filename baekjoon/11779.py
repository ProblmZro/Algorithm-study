# 기존 다익스트라 + 경로 저장
import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c)) # a->b 비용 c

start, end = map(int, input().split())

distance = [INF] * (n+1)
trace = [0] * (n+1) # 경로 저장용

def dijkstra(start):
  distance[start] = 0

  q = []
  heapq.heappush(q, (0, start)) # 거리, 노드

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for next, cost in graph[now]:
      new_dist = dist + cost
      if new_dist < distance[next]:
        distance[next] = new_dist
        trace[next] = now # 직전에 어디를 거쳐서 왔는지
        heapq.heappush(q, (new_dist, next))
  
  return distance

print(dijkstra(start)[end])

res = []
i = end
while i != 0:
  res.insert(0, i)  # 맨 앞에 넣기
  i = trace[i]

print(len(res))
print(*res)