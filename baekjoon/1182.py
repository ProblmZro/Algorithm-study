def backTacking(sum, idx):
  global cnt
  if idx >= n : return
  sum += arr[idx]
  if sum == s : cnt += 1
  backTacking(sum, idx+1)
  backTacking(sum-arr[idx], idx+1)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
sum = 0

backTacking(sum, 0)

print(cnt)