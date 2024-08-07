from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(N+1):
  graph[i].sort(reverse = True)

cnt = 1

def bfs(v):
  global cnt
  queue = deque([v])
  visited[v] = 1
  
  while queue:
    a = queue.popleft()

    for i in graph[a]:
      if visited[i] == 0:
        cnt += 1
        visited[i] = cnt
        queue.append(i)

bfs(R)

for i in range(1, N+1):
  print(visited[i])