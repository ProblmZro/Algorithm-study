from collections import deque

n, w, L = map(int, input().split()) # n 트럭의 수, w 다리 길이, L 최대하중
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)
total_weight = 0
time = 0

while trucks or total_weight > 0:
  time += 1
  total_weight -= bridge.popleft()

  if trucks:
    if total_weight + trucks[0] <= L:
      truck = trucks.popleft()
      bridge.append(truck)
      total_weight += truck
    else:
      bridge.append(0)

print(time)