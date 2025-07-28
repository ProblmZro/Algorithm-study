import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
  global res
  visited[v] = True
  team.append(v)
  next_mem = graph[v]
  if visited[next_mem]: # 다음 사람 이미 탐색했을 때
    if next_mem in team:  # 이미 멤버로 있을 때 (싸이클 생겼을 때)
      res -= len(team[team.index(next_mem):]) # 나온 요소 값의 인덱스 ~ 마지막
  else:
    dfs(next_mem)
    
for _ in range(int(input())):
  n = int(input())
  res = n
  graph = [0] + list(map(int, input().split()))
  visited = [False] * (n+1)
  for i in range(1, n+1):
    if not visited[i]:
      team = []
      dfs(i)

  print(res)