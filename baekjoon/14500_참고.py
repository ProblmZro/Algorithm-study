# 2차원 그래프 사이즈
N, M = 5, 5  # 예: 5x5 격자
board = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 상하좌우 방향
dx = [-1, 1, 0, 0]  # 위, 아래
dy = [0, 0, -1, 1] 

def dfs(x, y, depth):
  if depth == 4:
    print("블록:")
    for row in visited:
      print(row)
    print()
    return
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<N and 0<=ny<M and visited[nx][ny] != 1:
      visited[nx][ny] = 1
      dfs(nx, ny, depth+1)
      visited[nx][ny] = 0

visited[0][0] = 1
dfs(0,0, 1)