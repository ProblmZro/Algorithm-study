from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
melt_cnt = [[0 
for _ in range(M)] for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i, j):
  global res
  q = deque()
  q.append((i, j))
  res += 1

  while q:
    x, y = q.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k] 
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue  
      if graph[nx][ny] != 0 and visited[nx][ny] == 0:
        q.append((nx, ny))
        visited[nx][ny] = res

year = 0
while True:
  cnt = 0
  res = 0
  year += 1
  visited = [[0 for _ in range(M)] for _ in range(N)]

  for x in range(N):
    for y in range(M):
      if graph[x][y] != 0:
        cnt += 1
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
          if graph[nx][ny] == 0:
            melt_cnt[x][y] += 1

  if cnt == 0:
    print(0)
    break

  for i in range(N):
    for j in range(M):
      graph[i][j] -= melt_cnt[i][j]
      if graph[i][j] < 0 : graph[i][j] = 0
      melt_cnt[i][j] = 0

  for i in range(N):
    for j in range(M):
      if graph[i][j] > 0 and visited[i][j] == 0:
        bfs(i, j)
  
  if res >= 2:
    print(year)
    break