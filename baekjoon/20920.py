# 자주 나오는 거 -> 단어 긴 거 -> 사전 순
import sys
N, M = map(int, sys.stdin.readline().split())
words = {}

for _ in range(N):
  w = input()
  if len(w) >= M:
    if w not in words:
      words[w] = 0
    else:
      words[w] += 1

words = sorted(words.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in words:
  print(i[0])