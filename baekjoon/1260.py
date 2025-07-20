from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  m, n = map(int, input().split())
  graph[m].append(n)
  graph[n].append(m)

for i in range(1, N + 1):
  graph[i].sort() ##


visited = [False] * (N+1)
visited2 = [False] * (N+1)

def dfs(v, visited):
  visited[v] = True
  print(v, end=" ")

  for i in graph[v]:
    if not visited[i]:
      dfs(i, visited)

def bfs(v, visited):
  queue = deque([v])
  visited[v] = True

  while queue:
    cur = queue.popleft()
    print(cur, end=" ")

    for i in graph[cur]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

dfs(V, visited)
print()
bfs(V, visited2)