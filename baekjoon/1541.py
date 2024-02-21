import sys
input = sys.stdin.readline

exps = input().split("-")
sum_list = []

for exp in exps:
  sum = 0
  tmps = exp.split('+')
  for tmp in tmps:
    sum += int(tmp)
  sum_list.append(sum)

res = 0
for i in range(0, len(sum_list)):
  if i == 0 : res += sum_list[i]
  else : res -= sum_list[i]
print(res)


10-20-30+40

10

20

30+40
