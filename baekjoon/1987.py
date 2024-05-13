import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))
d = [(1,0), (-1,0), (0,1), (0,-1)]
ans = 0
alphas = set()

def dfs(x, y, cnt):
  global ans
  ans = max(ans, cnt)

  for i in range(4):
    nx = x + d[i][0]
    ny = y + d[i][1]
    if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in alphas:
      alphas.add(graph[nx][ny])
      dfs(nx, ny, cnt+1)
      alphas.remove(graph[nx][ny])

alphas.add(graph[0][0])
dfs(0, 0, 1)
print(ans)