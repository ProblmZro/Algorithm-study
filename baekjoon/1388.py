def dfs(x, y):
  visited[x][y] = True
  if graph[x][y] == '|':
    if x+1<N and graph[x+1][y] == '|' and visited[x+1][y] == False :
      dfs(x+1, y)
    else:
      return
  if graph[x][y] == '-':
    if y+1<M and graph[x][y+1] == '-' and visited[x][y+1] == False :
      dfs(x, y+1)
    else:
      return

N, M = map(int, input().split())

graph = []
visited = []
cnt = 0

for _ in range(N) :
  visited.append([False]*M)  
for _ in range(N) : 
  graph.append(list(input()))

for i in range(N) :
  for j in range(M) :
    if visited[i][j] == False:
      dfs(i, j)
      cnt += 1

print(cnt)