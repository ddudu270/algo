import sys

list = sys.stdin.readline().rstrip()
stack = []
result = 0

for i in range(len(list)):
    if list[i] == '(':
        stack.append(list[i])
    else:
        stack.pop()
        if list[i-1] == ')':
            result += 1
        else:
            result += len(stack)

print(result)