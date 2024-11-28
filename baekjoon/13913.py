from collections import deque

N, K = map(int, input().split())
max_pos = 100001
position = [0] * max_pos
check = [0] * max_pos

def trace(n):
  res = []
  while n != N:
    res.append(n)
    n = check[n]
  res.append(N)
  print(' '.join(map(str, res[::-1])))

def bfs(i, j):
  q = deque()
  q.append(i)
  
  while q:
    x = q.popleft()
    if x == j:
      print(position[x])
      trace(x)
      return 

    for dx in (x-1, x+1, 2*x):
      if 0 <= dx < max_pos and position[dx] == 0:
        position[dx] = position[x] + 1
        check[dx] = x
        q.append(dx)

bfs(N, K)