import sys
input = sys.stdin.readline

A, B = map(int, input().split())
res, tmp = 1, 0

while A != B:
  res += 1
  if B % 10 == 1:
    B //= 10
  elif B % 2 == 0 and B != 0:
    B //= 2
  else:
    print(-1)
    break
else:
  print(res)