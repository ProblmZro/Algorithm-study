infix = input()
stack = []
prior = {'*':3, '/':3, '+':2, '-':2, '(':1}

for s in infix:
  if s.isalpha():
    print(s, end="")
  elif s == '(':
    stack.append(s)
  elif s == ')':
    while stack[-1] != '(':
      print(stack.pop(), end="")
    stack.pop()
  else:
    while stack and prior[s] <= prior[stack[-1]]:
      print(stack.pop(), end="")
    stack.append(s)

while len(stack) != 0:
    print(stack.pop(), end="")


# 문자열 : 바로 출력
# 연산자 : 스택에 삽입 (맨 위에 있는 게 삽입하는 거보다 우선 순위면 스택에 있는 거 다 출력하고 삽입)
# 더이상 넣을 거 없으면 다 빼기