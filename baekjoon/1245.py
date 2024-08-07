from collections import deque

N, M = map(int, input().split())

cnt = 0
graph = []
visited = [[False] * M for _ in range(N)]

for _ in range(N):
  graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def bfs(start, end):
  global cnt
  queue = deque([(start, end)])
  isTop = True

  while queue:
    x, y = queue.popleft()
    visited[x][y] = True

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx>=0 and nx<N and ny>=0 and ny<M:
        if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
          queue.append((nx, ny))
        elif graph[x][y] < graph[nx][ny]:
          isTop = False
  
  if isTop:
    cnt += 1

for n in range(N):
  for m in range(M):
    if not visited[n][m]:
      bfs(n, m)

print(cnt)