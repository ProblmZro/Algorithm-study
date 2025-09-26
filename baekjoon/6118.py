from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

queue = deque()
queue.append((1,0))
visited[1] = True

res = []
while queue:
  nodes = queue.popleft()   # (node, dist)
  res.append(nodes)
  for next in graph[nodes[0]]:
    if visited[next] == False:
      queue.append((next, nodes[1]+1))
      visited[next] = True

res.sort(key=lambda x: (-x[1], x[0]))

res1 = res[0][0]
res2 = res[0][1]
res3 = 0

for i in res:
  if res2 == i[1]:
    res3 += 1

print(res1, res2, res3)