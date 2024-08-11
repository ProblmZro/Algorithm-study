from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
map = []
visited = [[0] * C for _ in range(R)]
dx=[1, 0, -1, 0]
dy=[0, -1, 0, 1]

for _ in range(R):
  map.append(list(input()))

def bfs(x, y):
  num_v = 0
  num_k = 0
  queue = deque()
  queue.append([x, y])

  while queue:
    x, y = queue.popleft()
    visited[x][y] = 1
    if map[x][y] == 'v':
      num_v += 1
    elif map[x][y] == 'k':
      num_k += 1

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<R and 0<=ny<C and visited[nx][ny] == 0 and map[nx][ny] != '#':
        visited[nx][ny] = 1
        queue.append([nx, ny])
    
  if num_k > num_v:
    num_v = 0
  else:
    num_k = 0

  return num_v, num_k

v, k = 0, 0
for n in range(R):
  for m in range(C):
    if not visited[n][m] and map[n][m] != '#':
      v_tmp, k_tmp = bfs(n, m)
      v += v_tmp
      k += k_tmp

print(k, v)