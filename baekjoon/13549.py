from collections import deque

N, K = map(int, input().split())
max_pos = 100001
position = [0] * max_pos

def bfs(i, j):
  q = deque()
  q.append(i)
  
  while q:
    x = q.popleft()
    if x == j:
      return position[x]

    if x == 0:
      position[1] = position[0] + 1
      q.append(1)
      continue

    for dx in 2*x, x-1, x+1:
      if 0 <= dx < max_pos and position[dx] == 0:
        if dx == 2*x:
          position[dx] = position[x]
          q.appendleft(dx)
        else:
          position[dx] = position[x] + 1
          q.append(dx)

print(bfs(N, K))