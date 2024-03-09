import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())))

for _ in range(R):
  for i in range(min(N, M) // 2):
    x, y = i, i
    tmp = arr[x][y]

    for j in range(1 + i, N - i):
      x = j
      prev = arr[x][y]
      arr[x][y] = tmp
      tmp = prev

    for j in range(1 + i, M - i):
      y = j
      prev = arr[x][y]
      arr[x][y] = tmp
      tmp = prev 

    for j in range(1 + i, N - i):
      x = N-j-1
      prev = arr[x][y]
      arr[x][y] = tmp
      tmp = prev

    for j in range(1 + i, M - i):
      y = M-j-1
      prev = arr[x][y]
      arr[x][y] = tmp
      tmp = prev

for i in range(N):
  for j in range(M):
    print(arr[i][j], end=' ')
  print()