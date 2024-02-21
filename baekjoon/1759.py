import sys
input = sys.stdin.readline

def DFS(start, vow_cnt, cons_cnt):
  if len(arr) == L:
    if vow_cnt >= 1 and cons_cnt >= 2:
      print(''.join(map(str, arr)))
    return

  for i in range(start, len(chars)):
    if chars[i] not in arr:
      if chars[i] in vowels:
        arr.append(chars[i])
        DFS(i + 1, vow_cnt + 1, cons_cnt)
        arr.pop()
      else:
        arr.append(chars[i])
        DFS(i + 1, vow_cnt, cons_cnt + 1)
        arr.pop()

L, C = map(int, input().split())
chars = input().split()
chars.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
arr = []
DFS(0, 0, 0)