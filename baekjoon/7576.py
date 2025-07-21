from collections import deque

M, N = map(int, input().split())
store = []
for _ in range(N):
  store.append(list(map(int, input().split())))
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
queue = deque([])

for i in range(N):
  for j in range(M):
    if store[i][j] == 1:
      queue.append([i, j])

def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<M and store[nx][ny] == 0:
        store[nx][ny] = store[x][y]+1
        queue.append((nx, ny))

bfs()

res = 0
for i in range(N):
  for j in range(M):
    if store[i][j] == 0:
      print(-1)
      exit()
    else :
      res = max(res, store[i][j]) 
print(res-1)
