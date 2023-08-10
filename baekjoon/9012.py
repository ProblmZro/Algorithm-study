n = int(input())
for _ in range(n):
  str_list = list(map(str, input()))
  stack = []
  value = True
  for s in str_list :
    if s == "(":
      stack.append(s)
    elif s == ")":
      if len(stack) == 0 or stack[-1] == ")" :
        value = False
        break
      else :
        stack.pop(-1)

  if not value or len(stack) > 0 : print("NO")
  else : print("YES")