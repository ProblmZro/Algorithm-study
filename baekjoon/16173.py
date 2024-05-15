N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
res = 0

def dfs(x, y):
  global res
  if x<0 or x>=N or y<0 or y>=N or visited[x][y]==1:
    return
  if graph[x][y] == -1:
    res = 1
    return 
  visited[x][y] = 1
  dfs(x+graph[x][y], y)
  dfs(x, y+graph[x][y])

dfs(0, 0)
print("HaruHaru") if res == 1 else print("Hing")