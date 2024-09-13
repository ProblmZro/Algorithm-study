X, Y = map(int, input().split())
Z = (Y * 100) // X

start = 0
end = X
res = 0

if Z >= 99:
  print(-1)
  exit()

while start <= end:
  mid = (start+end) // 2
  if ((Y+mid) * 100) // (X+mid) != Z:
    res = mid
    end = mid - 1
  else:
    start = mid + 1

print(res)