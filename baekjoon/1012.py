import sys
sys.setrecursionlimit(10**5)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  if x>=N or x<0 or y>=M or y<0:
    return False

  if graph[x][y] == 1:
    graph[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]  
      dfs(nx, ny)
    return True

  return False

for _ in range(int(input())):
  M, N, K = map(int, input().split())
  graph = [[0] * M for _ in range(N)]
  for _ in range(K):
    X, Y = map(int, input().split())
    graph[Y][X] = 1
  cnt = 0
  for i in range(N):
    for j in range(M):
      if dfs(i, j):
        cnt += 1
  print(cnt)

