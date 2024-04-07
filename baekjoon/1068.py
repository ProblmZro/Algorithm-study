N = int(input())
parent = list(map(int, input().split()))
delete = int(input())

def DFS(delete):
  parent[delete] = -2
  for i in range(N):
    if parent[i] == delete:
      DFS(i)

DFS(delete)
cnt = 0
for i in range(N):
  if parent[i] != -2 and i not in parent:
    cnt += 1

print(cnt)