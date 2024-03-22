N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
cnt = 0

def back(start):
  global cnt
  if sum(ans) == S and len(ans) > 0 :
    cnt += 1
  for i in range(start, N):
    ans.append(arr[i])
    back(i+1)
    ans.pop()      

back(0)
print(cnt)