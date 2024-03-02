S = input()
stack = []
Bracket = False

for i in S:
  if i == '<':
    Bracket = True
    for _ in range(len(stack)):
      print(stack.pop(), end='')
  
  stack.append(i)

  if i == '>':
    Bracket = False
    for _ in range(len(stack)):
      print(stack.pop(0), end='')

  if i == ' ' and not Bracket:
    stack.pop()
    for _ in range(len(stack)):
      print(stack.pop(), end='')
    print(' ', end='')


for _ in range(len(stack)):
  print(stack.pop(), end='')