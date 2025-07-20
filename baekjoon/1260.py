from collections import deque

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
  m, n = map(int, input().split())
  graph[m][n] = 1
  graph[n][m] = 1

visited = [False] * (N+1)
visited2 = [False] * (N+1)

def dfs(v, visited):
  visited[v] = True
  print(v, end=" ")

  for i in range(1, N+1):
    if (graph[v][i] == 1) and (not visited[i]):
      dfs(i, visited)

def bfs(v, visited):
  visited2[V] = True
  queue = deque([v])
  while queue:
    v = queue.popleft()
    print(v, end=" ")
    
    for i in range(1, N+1):
      if (graph[v][i] == 1) and (not visited[i]):
        queue.append(i)
        visited[i] = True

dfs(V, visited)
print()
bfs(V, visited2)


# {1: [2, 3, 4], 2: [4], 3: [4]}