import sys
sys.setrecursionlimit(100000)

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
for _ in range(K):
  x1, y1, x2, y2 = map(int, input().split())
  for x in range(x1, x2):
    for y in range(y1, y2):
      graph[y][x] = 1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dfs(x, y):
  global res
  graph[x][y] = -1
  res += 1
  
  for i in range(4):
    tx = dx[i] + x
    ty = dy[i] + y

    if (0<=tx<M and 0<=ty<N) and graph[tx][ty] == 0:
      dfs(tx, ty)

cnt = 0
res_list = []
for i in range(M):
  for j in range(N):
    if graph[i][j] == 0:
      res = 0
      dfs(i, j)
      cnt += 1
      res_list.append(res)

print(cnt)
print(*sorted(res_list))
