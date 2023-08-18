import sys
input = sys.stdin.readline

def binarySearch(arr, target, start, end) :
  if start > end:
    return end
  mid = (start + end) // 2
  cnt_num = [i // mid for i in arr]
  if sum(cnt_num) < target :
    return binarySearch(arr, target, start, mid-1)
  elif sum(cnt_num) >= target :
    return binarySearch(arr, target, mid + 1, end)

K, N = map(int, input().split())
num_list = [int(input()) for _ in range(K)]
res = binarySearch(num_list, N, 1, max(num_list))
print(res)