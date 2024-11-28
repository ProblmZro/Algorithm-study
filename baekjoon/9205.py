from collections import deque

def dist(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

def bfs(hx, hy, conv, px, py):
  q = deque()
  q.append((hx, hy))
  while q:
    x, y = q.popleft()
    if dist(x, y, px, py) <= 1000:
      return True
    for nx, ny in conv:
      if dist(x, y, nx, ny) <= 1000:
        q.append((nx, ny))
        conv.remove([nx, ny])
  return False

for _ in range(int(input())):
  n = int(input())
  hx, hy = map(int, input().split())
  conv = [list(map(int, input().split())) for _ in range(n)]
  px, py = map(int, input().split())

  if bfs(hx, hy, conv, px, py):
    print("happy")
  else:
    print("sad")
  
