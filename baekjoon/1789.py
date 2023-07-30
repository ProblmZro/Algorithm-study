n = int(input())
sum = 0
res = 0

for i in range(1, n+1) :
  sum += i
  res += 1
  if(sum > n) :
    res -= 1
    break

print(res)
