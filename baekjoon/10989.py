# sort 사용 : 메모리 초과
# 해결 방법 : 계수정렬
# n = int(input())
# l = []
# for _ in range(n) :
#   l.append(int(input()))
# l.sort()
# for i in l :
#   print(i)
import sys

n = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(n):
  arr[int(sys.stdin.readline())] += 1

for i in range(len(arr)):
 if arr[i] != 0 :
  for j in range(arr[i]):
    print(i)