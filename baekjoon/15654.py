def dfs():
  if len(ans) == m:
    print(' '.join(map(str, ans)))
    return
  for i in arr:
    if i not in ans:
      ans.append(i)
      dfs()
      ans.pop()

n, m = map(int, input().split())
ans = []
arr = [int(i) for i in input().split()]
arr.sort()
dfs()