n, m = map(int, input().split())
arr = []
size = 1

for _ in range(n):
  arr.append(str(input()))

for i in range(n):  # 0 1 2
  for j in range(m-1):  # 0 1 2 3
    for k in range(j+1, m): # 1~4 2~4 3~4 4
      if arr[i][j] == arr[i][k] == arr[i+k-j][j] == arr[i+k-j][k]:
        print((k-j+1)**2)
        # if (j-k+1)**2 > size :
        #   size = (j-k+1)**2

# print(size)