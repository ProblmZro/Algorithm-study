# 유클리드 호제법

# 최대공약수
def GCD(x, y):
  while(y):
    x, y = y, x % y
  return x

# 최소공배수
def LCM(x, y):
  res = (x * y) // GCD(x, y)
  return res


a, b = map(int, input().split())
print(GCD(a, b))
print(LCM(a, b))