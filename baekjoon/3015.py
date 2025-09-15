N = int(input())
people = []
for _ in range(N):
  people.append(int(input()))

cnt = 0
for i in range(N-1):
  a = people[i]
  b = people[i+1]
  cnt += 1
  for j in range(i+2, N):
    if a >= b:
      if b < people[j]:
        b = people[j]
      cnt += 1
    else: # a < b
      break

print(cnt)