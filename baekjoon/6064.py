def cal(M, N, x, y):
  k = x
  while k <= M*N:
    if (x-k)%M==0 and (y-k)%N==0  :
      return k
    k += M
  return -1

n = int(input())

for _ in range(0, n):
  M, N, x, y = map(int, input().split())
  print(cal(M, N, x, y))

# 1 1
# 2 2 
# 3 3 
# 4 4
# 5 5 
# 6 6
# 7 7
# 8 8
# 9 9 
# 10 10
# 11%10 11 -> 1 11
# 12%10 12 -> 2 12
# 13%10 13%12 -> 3 1
# 14%10 14%12 -> 4 2

# 10 12
# x = 1 -> 1 11 21 31 ... (a % M)
# y = 1 -> 1 13 25 37 ... (a % N)