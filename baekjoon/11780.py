INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
trace = [[-1] * (n+1) for _ in range(n+1)] # -1 : 못가는 경로

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = min(graph[a][b], c)
  trace[a][b] = a # 어디서 왔는지

for a in range(1, n+1):
  graph[a][a] = 0

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      new_path = graph[a][k]+graph[k][b]
      if new_path < graph[a][b]:
        graph[a][b] = new_path
        trace[a][b] = trace[k][b]

for i in range(1, len(graph)):
  print(*graph[i][1:])

for i in range(1, n+1):
  for j in range(1, n+1):
    if trace[i][j] == -1:
      print(0)
      continue

    tmp_j = j
    ans = []
    while True:
      if tmp_j==i:
        break
      ans.append(tmp_j)
      tmp_j = trace[i][tmp_j]
    print(len(ans)+1, i, *ans[::-1])  # 거꾸로