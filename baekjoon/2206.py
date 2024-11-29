from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j, k):
  q = deque()
  q.append((i, j, k))

  while q:
    x, y, z = q.popleft()
    
    if x == N-1 and y == M-1:
      return visited[x][y][z]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if maps[nx][ny] == 1 and z == 0:
        visited[nx][ny][1] = visited[x][y][0] + 1
        q.append((nx, ny, 1))
      elif maps[nx][ny] == 0 and visited[nx][ny][z] == 0:
        visited[nx][ny][z] = visited[x][y][z] + 1
        q.append((nx, ny, z))

  return -1

print(bfs(0, 0, 0))