m = int(input())
n = int(input())
graph = [[] for _ in range(m+1)]
visited = [0] * (m+1)

for _ in range(n):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

res = []

def dfs(v):
  visited[v] = True
  res.append(v)

  for i in graph[v]:
    if not visited[i]:
      dfs(i)

dfs(1)

print(len(res)-1)