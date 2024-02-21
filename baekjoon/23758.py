import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

mid = (N+1)//2
ans = 1
arr.sort()

for i in range(mid):
  while arr[i] > 1:
    arr[i] = arr[i]//2
    ans += 1

print(ans)

# 7 3 9 5
# 3 5 7 9 
# 2
# 2 3 7 9

# 2 3 7 9
# 1 2 7 9

# 1 2 7 9
# 1 1 7 9

# 0 1 7 9


