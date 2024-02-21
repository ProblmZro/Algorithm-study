import sys
input = sys.stdin.readline

M = int(input())
m = 10**M

for i in range(m//2):
  k = 1
  for j in range(i+1):
    k *= j
  if k//m < 10:
    print(i)
print(m)