def solution(s):
    stack = []
    for a in s:
        if a == '(':
            stack.append('a')
        elif a == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    if stack:
        return False
    else:
        return True