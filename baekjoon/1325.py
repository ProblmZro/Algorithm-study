# 시간초과 -> pypy로 풀림
# A -> B 신뢰 : B 해킹 -> A 해킹 가능
# A -> B 말고 반대로 저장
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  A, B = map(int, input().split())
  graph[B].append(A)

res = []
max_cnt = 0

for i in range(1, N+1):
  visited = [False] * (N+1)
  cnt = 0
  queue = deque()
  queue.append(i)
  visited[i] = True

  while queue:
    now = queue.popleft()
    for next in graph[now]:
      if not visited[next]:
        visited[next] = True
        queue.append(next)
        cnt += 1

  res.append((i, cnt))
  max_cnt = max(max_cnt, cnt)

for node, cnt in res:
  if cnt == max_cnt:
    print(node, end=' ')