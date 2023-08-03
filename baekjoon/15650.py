def dfs(start):
  if len(arr) == m: # 리스트 길이가 m과 동일해지면 리스트 출력
    print(' '.join(map(str, arr)))  # [1, 2] -> 1 2
    return
  for i in range(start, n+1): # 동일하지 않으면 for문 실행
    if i not in arr:  # 리스트에 i 없으면
      arr.append(i) # i 추가
      dfs(i+1)
      arr.pop() # 다 차면 리스트 비우기

n, m = map(int, input().split())
arr = []
dfs(1)


# 4 2
# 12 13 14 23 24 34