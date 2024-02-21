import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def Prime(n) :
  for i in range(2, int(n**(1/2))+1):
    if n%i == 0:
      return False
  return True

for i in range(M, N+1):
  if Prime(i): print(i)