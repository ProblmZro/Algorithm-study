from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  graph[x][y] = 0
  area = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        q.append((nx, ny))
        graph[nx][ny] = 0
        area += 1

  return area

cnt = 0
max_area = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      cnt += 1
      max_area = max(bfs(i, j), max_area)

print(cnt)
print(max_area)