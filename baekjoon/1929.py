M, N = map(int, input().split())

def isPrime(n) :
  if n == 1:
    return False
  for i in range(2, (n**0.5)+1):
    if n % i == 0:
      return False
  return True

for i in range(M, N+1):
  if isPrime(i) : print(i)