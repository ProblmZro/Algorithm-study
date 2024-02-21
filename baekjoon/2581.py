import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

def isPrime(n) : 
  if n == 1 :
    return False
  for i in range(2, int(n**(1/2))+1) :
    if(n % i == 0) :
      return False
  return True

sum = 0
min = 10000

for i in range(M, N+1):
  if isPrime(i) :
    sum += i
    if i < min : 
      min = i

if sum == 0 : 
  print(-1)
else : 
  print(sum)
  print(min)