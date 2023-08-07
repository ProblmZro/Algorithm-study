# 이분 탐색으로 풀기
def binary_search(arr, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for i in range(M):
    res = binary_search(A, B[i], 0, N - 1)
    if res is False:
        print(0)
    else:
        print(1)


'''
N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for b in B :
  if b in A : print(1)
  else : print(0)
'''