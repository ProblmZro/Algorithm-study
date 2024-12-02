N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

tn = 0
for s in size:
  if s == 0:
    continue
  elif T >= s:
    tn += 1
  elif s % T == 0:
    tn += s//T
  else:
    tn += s//T + 1

print(tn)
print(N//P, N%P)