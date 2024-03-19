import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
mal = list(map(str, input().split()))

ans = abs(100 - N)

for num in range(1000001):
  for n in str(num):
    if n in mal:
      break
  else:
    ans = min(len(str(num)) + abs(num-N), ans)

print(ans)