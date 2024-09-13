N, M = map(int, input().split())
lectures = list(map(int, input().split()))

start = max(lectures)
end = sum(lectures)
res = sum(lectures)

while start <= end:
  mid = (start + end) // 2

  cnt = 1
  total = 0
  for l in lectures:
    if total + l > mid:
      cnt += 1
      total = 0
    total += l
  
  if cnt > M :
    start = mid + 1
  else:
    res = min(mid, res)
    end = mid - 1

print(res)