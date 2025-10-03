from collections import deque

N = int(input())
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
graph = [list(input()) for _ in range(N)]

def bfs(start, target, n, visited):
  queue = deque()
  queue.append(start)

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      dx, dy = x+direct[i][0], y+direct[i][1]
      if 0<=dx<N and 0<=dy<N and visited[dx][dy] == 0:
        if graph[dx][dy] == target:
          visited[dx][dy] = n
          queue.append((dx, dy))

res = 1
for i in range(N):
  for j in range(N):
    if visited1[i][j] == 0:
      target = graph[i][j]
      bfs((i, j), target, res, visited1)
      res += 1

# 적록 색약
for i in range(N):
    for j in range(N):
      if graph[i][j] == 'G':
        graph[i][j] = 'R'

res2 = 1
for i in range(N):
  for j in range(N):
    if visited2[i][j] == 0:
      target = graph[i][j]
      bfs((i, j), target, res, visited2)
      res2 += 1

print(res-1, res2-1)