import heapq
import sys
input = sys.stdin.readline

N = int(input())
card = [int(input()) for _ in range(N)]
card.sort()

res = 0
while len(card) > 1:
  a = heapq.heappop(card)
  b = heapq.heappop(card)
  res += (a+b)
  heapq.heappush(card, a+b)

print(res)


# 30 40
# 10 20 40
# 30 70 -> 100
# 10 -> 10+20

# 10 20 30 40
# 30 60 100 -> 190

# 1 1 1 1
# 2 2 4 -> 8

# 1 2 3 100
# 3 6 106 -> 115

# 70 80 90 100
# 150 190 340 -> 680