from collections import deque

C = int(input())
N = int(input())
graph = [[] for _ in range(C+1)]
visited = [False for _ in range(C+1)]

for _ in range(N):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def BFS(start):
  queue = deque([start])
  cnt = 0
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        cnt += 1
  return cnt

print(BFS(1))
