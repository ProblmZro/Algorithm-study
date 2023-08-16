def dfs(num):
  if len(ans) == m:
    print(' '.join(map(str, ans)))
    return
  for i in range(num, n):
    ans.append(arr[i])
    dfs(i)
    ans.pop()

n, m = map(int, input().split())
ans = []
arr = [int(i) for i in input().split()]
arr.sort()
dfs(0)