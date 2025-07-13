N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for target in arr2:
  start, end = 0, N-1
  isIn = False

  while start <= end:
    mid = (start + end) // 2
    if arr1[mid] < target:
      start = mid+1
    elif arr1[mid] > target:
      end = mid-1
    else:
      isIn = True
      break
    
  if isIn:
    print(1, end = ' ')
  else:
    print(0, end = ' ')


# -10 2 3 6 10