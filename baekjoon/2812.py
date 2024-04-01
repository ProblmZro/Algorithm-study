N, K = map(int, input().split())
num = list(input())
stack = []

for n in num:
  while stack and stack[-1] < n and K > 0:
    stack.pop()
    K -= 1
  stack.append(n)

print(''.join(stack[:len(stack) - K]))


# 4 1 -> [4, 1]
# 4 7 -> []
# 7 7 -> [7, 7]
# 7 2 -> [7, 7]
# [4]

# 1 5 4 3
# 1 5 -> [5]
# 5 4 -> [5]
# [5, 3]
# stack=[5]

# stack에 들어갈 수가 더 크면 change, 아니면 그냥 넣기