from collections import deque

N, K = map(int, input().split())
visited = [0] * (100000+1)

def bfs(v):
  visited[v] = 0
  queue = deque([v])

  while queue:
    cur = queue.popleft()
    if cur == K:
      print(visited[cur])
      break
    for i in (cur-1, cur+1, cur*2):
      if 0<=i<=100000 and not visited[i]:
        queue.append(i)
        visited[i] = visited[cur]+1

bfs(N)

# 0 1 -> 2 예외