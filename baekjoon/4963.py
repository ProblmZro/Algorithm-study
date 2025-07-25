import sys
sys.setrecursionlimit(100000)

dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [1, -1, -1, 0, 1, -1, 0, 1]

def dfs(x, y):
  graph[x][y] = -1

  for i in range(8):
    tx = x + dx[i]
    ty = y + dy[i]
    if (0<=tx<h and 0<=ty<w) and (graph[tx][ty] == 1):
      dfs(tx, ty)

while True:
  w, h = map(int, input().split())
  if w==0 and h==0: break
  graph = []
  for _ in range(h):
    graph.append(list(map(int, input().split())))

  cnt = 0
  for x in range(h):
    for y in range(w):
      if graph[x][y] == 1:
        dfs(x, y)
        cnt += 1

  print(cnt)