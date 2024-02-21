import sys
input = sys.stdin.readline

N = int(input())

def isPrime(n):
  for i in range(2, int(n**(1/2))+1):
    if (n % i == 0) : 
      return False
  return True

def dfs(n):
  if len(str(n)) == N:
    print(n)
  else:
    for i in range(1, 10):
      tmp = n*10 + i
      if isPrime(tmp) : 
        dfs(tmp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)