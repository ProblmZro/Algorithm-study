import heapq
import sys
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort()

heap = [time[0][1]]
for i in range(1, N):
  if heap[0] <= time[i][0]:
    heapq.heappop(heap)
  heapq.heappush(heap, time[i][1])

print(len(heap))