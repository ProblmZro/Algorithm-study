def dfs():
  if len(ans) == m:
    print(' '.join(map(str, ans)))
    return
  for i in range(0, n):
    ans.append(arr[i])
    dfs()
    ans.pop()

n, m = map(int, input().split())
ans = []
arr = [int(i) for i in input().split()]
arr.sort()
dfs()