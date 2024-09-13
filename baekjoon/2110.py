N, C = map(int, input().split())
houses = []
for _ in range(N):
  houses.append(int(input()))

houses.sort()

start = 1
end = houses[-1] - houses[0]
ans = []

while start <= end:
  cnt = 1
  mid = (start + end) // 2
  curr = houses[0]

  for i in range(1, len(houses)):
    if curr + mid <= houses[i]:
      curr = houses[i]
      cnt += 1
  
  if cnt < C:
    end = mid - 1
  else:
    start = mid + 1
    ans.append(mid)

print(max(ans))