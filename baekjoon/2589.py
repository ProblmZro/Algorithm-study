from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
  visited = [[0] * M for _ in range(N)]
  q = deque()
  q.append((i, j))
  visited[i][j] = 1
  distance = 0

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if graph[nx][ny] == 'L' and visited[nx][ny] == 0:
        visited[nx][ny] = visited[x][y] + 1
        distance = max(distance, visited[nx][ny])
        q.append((nx, ny))

  return distance - 1

res = 0
for i in range(N):
  for j in range(M):
    if graph[i][j] == 'L':
      res = max(res, bfs(i, j))

print(res)