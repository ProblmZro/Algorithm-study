import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def Power(A, B, C):
  if B == 1 : 
    return A % C
  else : 
    x = Power(A, B//2, C)
    if B % 2 == 0:
      return x*x % C
    else :
      return x*x*A % C

print(Power(A,B,C))