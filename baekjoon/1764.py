N, M = map(int, input().split())
n_list = set()
ans_list = []
for _ in range(N):
  n_list.add(input())

for _ in range(M):
  m = input()
  if m in n_list:
    ans_list.append(m)

ans_list.sort()
print(len(ans_list))
for ans in ans_list:
  print(ans)