from collections import deque

N = int(input())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

# 섬 구분 저장 -> 다른 섬까지 가는 거 확인

# 1. bfs 돌면서 저장 (2~)
def bfs(x, y, cnt):
  queue = deque([(x, y)])
  graph[x][y] = cnt
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 1:
        graph[nx][ny] = cnt
        queue.append((nx, ny))

cnt = 2
for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      bfs(i, j, cnt)
      cnt += 1


# 2. 모든 섬에서 다른 섬 가는 거 확인
def bfs2(n):
  queue = deque([])
  dist = [[-1] * N for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if graph[i][j] == n: 
          dist[i][j] = 0
          queue.append((i, j))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<N:
        # 아직 미방문한 바다
        if (graph[nx][ny] == 0 and dist[nx][ny] == -1):
          dist[nx][ny] = dist[x][y] + 1
          queue.append((nx, ny))
        # 다른 섬 도착
        if (graph[nx][ny] > 0 and graph[nx][ny] != n):
          return dist[x][y]
  
  return int(1e9)

ans = int(1e9)
for n in range(2, cnt):
  tmp = bfs2(n)
  ans = min(ans, tmp)

print(ans)