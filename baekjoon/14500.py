N, M = map(int, input().split())
board = []
for _ in range(N):
  row = list(map(int, input().split()))
  board.append(row)
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

res = 0

def dfs(x, y, depth, total):
  global res
  if depth == 4:
    res = max(res, total)
    return
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<N and 0<=ny<M and visited[nx][ny] != 1:
      visited[nx][ny] = 1
      dfs(nx, ny, depth+1, total+board[nx][ny])
      visited[nx][ny] = 0

def extra_shape(x, y):
  global res
  shapes = [
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(0, 0), (1, -1), (1, 0), (1, 1)], # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, -1)]  # ㅓ
  ]
  for shape in shapes:
    total = 0
    valid = True
    for dx, dy in shape:
      nx = x + dx
      ny = y + dy
      if 0<=nx<N and 0<=ny<M:
        total += board[nx][ny]
      else:
        valid = False
        break
    if valid:
      res = max(res, total)
                
for x in range(N):
  for y in range(M):
    visited[x][y] = 1
    dfs(x,y,1, board[x][y])
    visited[x][y] = 0
    extra_shape(x, y)
print(res)