n = int(input())
nums = map(int, input().split())
p = 0
for num in nums :
  isPrime = 0
  if num > 1 :
    for i in range(2, num) :
      if (num % i == 0) :
        isPrime += 1
    if isPrime == 0 :
      p += 1
print(p)