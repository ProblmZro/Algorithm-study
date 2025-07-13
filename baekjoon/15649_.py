N, M = map(int, input().split())
arr = []
visited = [False] * (N+1)


def backTracking(arr, visited):
  if len(arr) == M:
    for a in arr:
      print(a, end=" ")
    print()
    return
  for i in range(1, N+1):
    if not visited[i]:
      visited[i] = True
      arr.append(i)
      backTracking(arr, visited)
      visited[i] = False
      arr.pop()

backTracking(arr, visited)


# 입력 : 4 2 
'''
  1 2
  1 3
  1 4
  2 1
  2 3
  2 4
  3 1
  3 2
  3 4
  4 1
  4 2
  4 3
'''