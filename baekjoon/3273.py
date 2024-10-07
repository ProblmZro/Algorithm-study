n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
start, end = 0, n-1
res = 0
while start < end:
  tmp = arr[start] + arr[end]
  if tmp < x:
    start += 1
  elif tmp > x:
    end -= 1
  else:
    res += 1
    start += 1

print(res)


# 1 2 3 5 7 9 10 11 12