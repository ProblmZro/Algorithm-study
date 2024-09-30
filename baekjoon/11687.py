import sys
input = sys.stdin.readline

M = int(input())

def count_zero(n):
  res = 0
  while n >= 5:
    n //= 5
    res += n
  return res

start, end = 0, 10**9
res = -1
while start <= end:
  mid = (start + end) // 2
  zero = count_zero(mid)
  if zero == M:
    res = mid
    end = mid - 1
  elif zero < M:
    start = mid + 1
  else:
    end = mid - 1

print(res)