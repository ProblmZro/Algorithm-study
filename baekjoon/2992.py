def dfs(res, idx):
  if res >= x: 
    print(0)
    return
  if idx >= len(arr): return
  res += arr[idx]*(10)**idx
  dfs(res, idx+1)




x = int(input())
arr = list(map(int, str(x)))
