prime = [False] * 2 + [True] * (1299709 - 1)

for i in range(1, 1299709 + 1):
  if not prime[i]:
    continue
  for j in range(i**2, 1299709 + 1, i):
    prime[j] = False

for _ in range(int(input())):
  k = int(input())
  start, end = k, k
  if not prime[k]:
    while not prime[start]:
      start -= 1
    while not prime[end]:
      end += 1
  print(end-start)