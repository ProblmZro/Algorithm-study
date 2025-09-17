from collections import deque

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  visited[x][y] = True
  cnt = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<N and 0<=ny<N:
        if graph[nx][ny] == 1 and not visited[nx][ny]:
          queue.append((nx, ny))
          visited[nx][ny] = True
          cnt += 1
  return cnt

res = []
for i in range(N):
  for j in range(N):
    if graph[i][j] == 1 and not visited[i][j]:
        res.append(bfs(i, j))

res.sort()
print(len(res))
for i in res:
 print(i)