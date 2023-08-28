N = int(input())
P = list(map(int, input().split()))
P.sort()
sum = 0
for i in range(len(P)) :
  for j in range(i+1) :
    sum += P[j]
print(sum)