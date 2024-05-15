def dfs(x, y, depth, cnt):
  visited[x][y] = True
  if graph[x][y] == 1:
    cnt += 1
  if cnt >= 2:
    return 1
  if depth >= 3:
      visited[x][y] = False
      return 0

  for i in range(4):
    xA = x + xD[i]
    yA = y + yD[i]
    if 0 <= xA <= 4 and 0 <= yA <= 4:
      if not visited[xA][yA] and graph[xA][yA] != -1:
        if dfs(xA, yA, depth+1, cnt) == 1:
          return 1
    visited[x][y] = False
    return 0

graph = [list(map(int, input().split())) for _ in range(5)]
visited = [[False for _ in range(5)] for _ in range(5)]
x, y = map(int, input().split())
xD = [0, 1, -1, 0]
yD = [1, 0, 0, -1]

print(dfs(x, y, 0, 0))