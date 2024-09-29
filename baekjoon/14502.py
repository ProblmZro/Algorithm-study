from collections import deque 
import copy

N, M = map(int, input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
  queue = deque()
  graph_tmp = copy.deepcopy(graph)

  for i in range(N):
    for j in range(M):
      if  graph_tmp[i][j] == 2:
        queue.append((i, j))

  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= 0 and nx < N and ny >= 0 and ny < M:
        if graph_tmp[nx][ny] == 0:
          graph_tmp[nx][ny] = 2
          queue.append((nx, ny))

  cnt = 0  
  global ans
  for i in range(N):
    cnt += graph_tmp[i].count(0)
  
  ans = max(ans, cnt)


def wall(cnt):
  if cnt == 3:
    bfs()
    return

  for i in range(N):
    for j in range(M):
      if graph[i][j] == 0:
        graph[i][j] = 1
        wall(cnt + 1)
        graph[i][j] = 0

ans = 0
wall(0)
print(ans)