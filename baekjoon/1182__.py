N, S = map(int, input().split())

num_arr = list(map(int, input().split()))
# num_arr.sort()

ans = []
cnt = 0
# visited : 순서 상관없이 원소를 뽑느냐 마느냐가 중요하며, 방문 여부와 관계없음

def backTracking(idx):
  global cnt
  if len(ans) != 0 and sum(ans) == S:
    cnt += 1   
    # return 없앰 ([-3, 3]이 S를 만족해도 [-3, 3, 0]도 탐색해야 함)

  for i in range(idx, N):
    ans.append(num_arr[i])
    backTracking(i+1)
    ans.pop()

backTracking(0)
print(cnt)