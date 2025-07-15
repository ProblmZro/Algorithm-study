N = int(input())
province = list(map(int, input().split()))
M = int(input())
province.sort()
start, end = 0, province[-1]

while start <= end:
  goal = M
  mid = (start + end) // 2
  for p in province:
    if p <= mid:
      goal -= p
    else:
      goal -= mid
  if goal < 0:
    end = mid - 1
  else:
    res = mid
    start = mid + 1

print(mid)