def Pulling(n, arr) : 
  if n == 1:
    return arr[0][0]
  new_mat = [[] for _ in range(n//2)]
  for i in range(0, n, 2):
    for j in range(0, n, 2):
      new_mat[i//2].append(sorted([arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]])[2])
  return Pulling(n//2, new_mat)

N = int(input())
mat = [(list(map(int, input().split()))) for _ in range(N)]

print(Pulling(N, mat))