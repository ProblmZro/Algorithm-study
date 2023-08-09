def binary_search(arr, target, start, end):
  if start > end:
    return 0
  mid = (start + end) // 2
  if arr[mid] == target:
      return cnt_dic.get(target)
  elif arr[mid] > target:
      return binary_search(arr, target, start, mid - 1)
  else:
      return binary_search(arr, target, mid + 1, end)

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()
cnt_dic = {}
for n in N_list:
  if n not in cnt_dic:
    cnt_dic[n] = 1
  else:
    cnt_dic[n] += 1

for i in range(M):
  res = binary_search(N_list, M_list[i], 0, N-1)
  print(res, end=" ")