from collections import deque

N,K = map(int,input().split())
queue = deque([i for i in range(1, N+1)])

res = []
while len(queue) != 0 :
  for i in range(K-1):
    queue.append(queue.popleft())
  # res에 추가와 동시에 queue에서 삭제
  res.append(str(queue.popleft()))

print('<'+', '.join(res)+'>')