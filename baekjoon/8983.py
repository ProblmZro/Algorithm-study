M, N, L = map(int, input().split())
station = sorted(list(map(int, input().split())))
animals = []
ans = 0

for _ in range(N):
  a, b = map(int, input().split())
  animals.append((a, b))

for x, y in animals:
  start, end = 0, len(station)-1
  mid = 0
  while start < end:
    mid = (start + end) // 2
    if station[mid] > x:
      end = mid - 1
    elif station[mid] < x:
      start = mid + 1
    else:
      start = mid
      break 
  if abs(station[start] - x) + y <= L:
    ans += 1
  elif start+1 < len(station) and abs(station[start+1] - x) + y <= L:
    ans += 1
  elif start > 0 and abs(station[start-1] - x) + y <= L:
    ans += 1

print(ans)