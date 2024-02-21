import sys
input = sys.stdin.readline

def gcd(m, n):
  if m < n : 
    m, n = n, m
  if n == 0 :
    return m
  if m % n == 0 :
    return n
  else :
    return gcd(n, m%n)

A, B = map(int, input().split())
C, D = map(int, input().split())

a = (A*D) + (B*C)
b = (B*D)

x = gcd(a, b)

print(a//x, b//x)