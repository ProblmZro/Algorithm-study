def dfs(start) :
  if len(arr) == M:
    print(' '.join(map(str, arr)))
    return
  for i in range(start, N+1):
    arr.append(i)
    dfs(i)
    arr.pop()

N, M = map(int, input().split())
arr = []
dfs(1)

# 입력 : 4 2 
'''
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
'''
