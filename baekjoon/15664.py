def dfs(depth, num):
  if depth == M:
    print(' '.join(map(str, ans)))
    return
  dup = 0
  for i in range(num, N):
    if not visited[i] and dup != arr[i]:
      visited[i] = True
      ans.append(arr[i])
      dup = arr[i]
      dfs(depth+1, i)
      visited[i] = False
      ans.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False] * N
ans = []

dfs(0, 0)