def dfs(i):
  visited[i] = 1
  tmp = P[i]

  if visited[tmp] == 0:
    dfs(tmp)
    
  return

for _ in range(int(input())):
  N = int(input())
  P = [0] + list(map(int, input().split()))
  visited = [0] * (N+1)
  cnt = 0

  for i in range(1, N+1):
    if visited[i] == 0:
      dfs(i)
      cnt += 1

  print(cnt)