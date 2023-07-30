n, m = map(int, input().split())
arr = []
size = 1

for _ in range(n):
  arr.append(str(input()))

for i in range(n-1):
  for j in range(m-1):
    for k in range(j+1, m):
      if i+k-j < n : 
        if arr[i][j] == arr[i][k] == arr[i+k-j][j] == arr[i+k-j][k]:
          if (k-j+1)**2 > size :
            size = (k-j+1)**2

print(size)