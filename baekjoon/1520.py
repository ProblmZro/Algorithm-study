M, N = map(int, input().split())
graph = []
for _ in range(M):
  graph.append(list(map(int, input().split())))
dp = [[-1]*N for _ in range(M)]
dx = [0, 1, 0, -1]
dy = [1, 0 , -1, 0]

def sol(x, y):
  if x==M-1 and y == N-1:
    return 1
  if dp[x][y] == -1:
    dp[x][y] = 0  # 방문 처리
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<M and 0<=ny<N and graph[nx][ny] < graph[x][y]:
        dp[x][y] += sol(nx, ny)

  return dp[x][y]

print(sol(0, 0))