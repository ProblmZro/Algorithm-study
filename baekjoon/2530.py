h, m, s = map(int, input().split())
n1 = int(input())

s += n1
m += s//60
h += m//60

print(h%24, m%60, s%60)