def dfs(stack, idx):
  if len(stack) == 6:
    print(' '.join(map(str, stack)))
    return

  for i in range(idx, k):
    stack.append(s[i])
    dfs(stack, i+1)
    stack.pop()  
  
while True:
  arr = list(map(int, input().split()))
  k = arr[0]
  s = arr[1:]
  stack = []
  dfs(stack, 0)
  if k == 0: break
  print()