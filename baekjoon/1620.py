import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(1, N+1):
  a = input().rstrip()
  dic[i] = a
  dic[a] = i

for _ in range(M):
  temp = input().rstrip()
  if temp.isdigit():
    print(dic[int(temp)])
  else :
    print(dic[temp])