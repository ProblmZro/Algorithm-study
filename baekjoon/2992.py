def dfs(lst, visited):
  if len(lst) == len(arr):
    qwe.append(int("".join(map(str, lst))))
    return
  
  for i in range(len(arr)):
    if not visited[i]:
      lst.append(arr[i])
      visited[i] = True 
      dfs(lst, visited)
      visited[i] = False
      lst.pop()

x = int(input())  # 156
arr = list(map(int, str(x)))  # [1, 5, 6]
visited = [False] * len(arr) # [F, F, F]

qwe = []
isFind = False

dfs([], visited)
qwe.sort()

for i in qwe:
  if i>x :
    print(i)
    isFind = True
    break
if not isFind: print(0)