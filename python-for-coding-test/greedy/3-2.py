n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
res = 0

while True:
  for i in range(k):
    if m == 0: break
    res += arr[-1]
    m -= 1
  if m == 0: break
  res += arr[-2]
  m -= 1

print(res)