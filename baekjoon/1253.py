N = int(input())
A = list(map(int, input().split()))
A.sort()

res = 0
for i in range(N):
  target = A[i]
  start, end = 0, len(A)-1
  while start < end:
    if A[start] + A[end] == target:
      if start == i:
        start += 1
      elif end == i:
        end -= 1
      else:
        res += 1
        break
    elif A[start] + A[end] > target:
      end -= 1
    elif A[start] + A[end] < target:
      start += 1

print(res)