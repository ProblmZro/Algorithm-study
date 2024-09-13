import sys
sys.setrecursionlimit(10**5)

def dfs(i):
  visited[i] = True
  for j in graph[i]:
    if not visited[j]:
      visited[j] = True
      dfs(j)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, N+1):
  if not visited[i]:
    dfs(i)
    cnt += 1

print(cnt)