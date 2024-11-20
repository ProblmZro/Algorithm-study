N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(x, cnt):
  global res
  if cnt == 4:
    res = 1
    return
  visited[x] = 1
  for i in graph[x]:
    if visited[i] == 0:
      dfs(i, cnt+1)
  visited[x] = 0


for i in range(N):
  visited = [0] * N
  cnt = 0
  res = 0
  dfs(i, cnt)
  if res == 1:
    print(1)
    break

else:
  print(0)