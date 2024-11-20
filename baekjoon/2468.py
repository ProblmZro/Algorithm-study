from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_value = max(max(row) for row in graph)

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def bfs(a, b, n):
  queue = deque()
  queue.append((a, b))
  visited[a][b] = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < N:
        if graph[nx][ny] > n and visited[nx][ny] == 0:
          visited[nx][ny] = 1
          queue.append((nx, ny))


res = 0
for n in range(max_value):
  visited = [[0] * N for _ in range(N)]
  cnt = 0

  for i in range(N):
    for j in range(N):
      if graph[i][j] > n and visited[i][j] == 0:
        bfs(i, j, n)
        cnt += 1

  res = max(res, cnt)

print(res)