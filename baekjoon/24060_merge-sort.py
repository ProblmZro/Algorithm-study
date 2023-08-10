# 병합 정렬 (다시 보기)
def merge_sort(lst) :
  if len(lst) == 1: return lst

  mid = (len(lst) + 1) // 2

  left_list = merge_sort(lst[:mid])
  right_list = merge_sort(lst[mid:])

  a, b = 0, 0
  tmp = []

  while a < len(left_list) and b < len(right_list):
    if left_list[a] < right_list[b]:
      tmp.append(left_list[a])
      ans.append(left_list[a])
      a += 1
    else :
      tmp.append(right_list[b])
      ans.append(right_list[b])
      b += 1
  while a < len(left_list):
    tmp.append(left_list[a])
    ans.append(left_list[a])
    a += 1
  while b < len(right_list):
    tmp.append(right_list[b])
    ans.append(right_list[b])
    b += 1
  
  return tmp

N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = []
merge_sort(A)

if len(ans) >= K:
  print(ans[K-1])
else:
  print(-1)