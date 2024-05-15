def dfs(x, y):
  if x<0 or x>=N or y<0 or y>=N:
    return False
  
  if graph[x][y] == 1:
    global cnt
    cnt += 1
    graph[x][y] = 0
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  
  return False

N = int(input())
cnt = 0
res = []
graph = [list(map(int, input())) for _ in range(N)]

for i in range(N):
  for j in range(N):
    if dfs(i,j) == True:
      res.append(cnt)
      cnt = 0

res.sort()
print(len(res))
for i in range(len(res)):
  print(res[i])