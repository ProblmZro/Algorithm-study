from collections import deque

card = [i for i in range(1, int(input())+1)]
deque = deque()

deque.extend(card)
while len(deque) != 1 :
  deque.popleft()
  deque.rotate(-1)

print(deque[0])