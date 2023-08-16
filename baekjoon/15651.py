def dfs():
  if len(arr) == m: # 리스트 길이가 m과 동일해지면 리스트 출력
    print(' '.join(map(str, arr)))  # [1, 2] -> 1 2
    return
  for i in range(1, n+1): # 동일하지 않으면 for문 실행
    arr.append(i) # i 추가
    dfs()
    arr.pop() # 다 차면 리스트 비우기

n, m = map(int, input().split())
arr = []
dfs()

# 입력 : 4 2 
'''
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
'''