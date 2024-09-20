N, K = map(int, input().split())
levels = []
for _ in range(N):
  levels.append(int(input()))

start = min(levels)
end = start + K

res = 0
while start <= end:
  mid = (start + end) // 2
  tmp = 0
  for level in levels:
    if level < mid:
      tmp += mid - level
  if tmp <= K:
    start = mid + 1
    res = max(mid, res)
  else:
    end = mid - 1

print(res)