from collections import deque

field = [list(input()) for _ in range(12)]

def down():
  for y in range(6):
    for x in range(10, -1, -1):
      for k in range(11, x, -1):
        if field[x][y] != "." and field[k][y] == ".":
          field[k][y] = field[x][y]
          field[x][y] = "."

dx = [0, 0, -1, 1]
dy = [1, -1, 0 ,0]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  break_blocks = [(x,y)]

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 12 and 0 <= ny < 6 and field[nx][ny] == field[x][y] and not visited[nx][ny]:
        queue.append((nx, ny))
        visited[nx][ny] = True
        break_blocks.append((nx, ny))
  return break_blocks

def delete(break_blocks):  
  for x, y in break_blocks:
    field[x][y] = '.'

res = 0
while True:
  isBreak = False
  visited = [[False] * 6 for _ in range(12)]

  for x in range(12):
    for y in range(6):
      if field[x][y] != "." and not visited[x][y]:
          same_blocks = bfs(x, y)
          if len(same_blocks) >= 4:
            isBreak = True
            delete(same_blocks)

  if isBreak:
    down()
    res += 1
  else:
    break
 
print(res)