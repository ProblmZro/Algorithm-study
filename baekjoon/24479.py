import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(N+1):
  graph[i].sort()

cnt = 1
def dfs(v):
  global cnt
  visited[v] = cnt
  for i in graph[v]:
    if visited[i] == 0:
      cnt += 1
      dfs(i)

dfs(R)

for i in range(1, N+1):
  print(visited[i])