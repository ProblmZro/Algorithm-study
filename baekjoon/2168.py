def gcd(a, b):
  if b > a: a, b = b, a
  while b > 0:
    c = a % b
    a, b = b, c
  return a

x, y = map(int, input().split())
print(x + y - gcd(x, y))