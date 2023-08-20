def dfs(depth):
  if depth == M:
    print(' '.join(map(str, ans)))
    return
  dup = 0
  for i in range(0, N):
    if dup != arr[i]:
      ans.append(arr[i])
      dup = arr[i]
      dfs(depth+1)
      ans.pop()

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

dfs(0)