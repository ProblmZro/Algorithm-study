N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))  ## 여기까진 다 동일

# # 방법 1 - 파이썬 내장 함수 사용
# arr.sort()
# for i in arr:
#   print(i)

# # 방법 2 - 버블 정렬
# for i in range(N-1): # (총 배열 길이 - 1)만큼 반복해야 함
#   for j in range(len(arr)-1):
#     if arr[j] > arr[j+1]:
#       arr[j], arr[j+1] = arr[j+1], arr[j]

# for i in arr:
#   print(i)

# 방법 3 - 삽입 정렬
for i in range(1, N):
  key = arr[i]  # 이번에 삽입할 값
  j = i-1
  while j>=0 and arr[j] > key:  # 삽입할 거 앞 부분과 비교해서 더 작으면 삽입
    arr[j+1] = arr[j]
    j -= 1
  arr[j+1] = key