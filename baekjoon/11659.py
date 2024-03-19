import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0]
sum_val = 0

for i in arr:
  sum_val += i
  prefix.append(sum_val)

for _ in range(M):
  i, j = map(int, input().split())
  print(prefix[j] - prefix[i-1])