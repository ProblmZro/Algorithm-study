def dfs(x, y, depth, score):
  global res

  if depth >= 3:
    if score >= 2:
      res = 1
  
  else:
    for i in range(4):
      xA = x + xD[i]
      yA = y + yD[i]
      if xA >= 5 or yA >= 5 or xA < 0 or yA < 0:
        continue
      if graph[xA][yA] == -1:
        continue
      if graph[xA][yA] == 1:
        dfs(x, y, depth+1, score+1)
        graph[x][y] = -1
      else :
        dfs(x, y, depth+1, score)
        graph[x][y] = -1


graph = [list(map(int, input().split())) for _ in range(5)]
x, y = map(int, input().split())
xD = [0, 1, -1, 0]
yD = [1, 0, 0, -1]

res = 0
dfs(x, y, 0, 0)
print(res)