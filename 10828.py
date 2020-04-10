import sys

num = int(sys.stdin.readline().rstrip())
stack = []

for i in range(num):
    com = sys.stdin.readline().rstrip().split()
    if com[0] == 'top':
        if stack: # 스택에 무언가 있다면
            print(stack[-1])
        if not stack: # 스택이 비었다면
            print(-1)
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'pop':
        if stack:  # 스택에 무언가 있다면
            print(stack.pop())
        else:  # 스택이 비었다면
            print(-1)
    elif com[0] == 'empty':
        if stack: # 스택에 무언가 있다면
            print(0)
        if not stack: # 스택이 비었다면
            print(1)
    else: # push의 경우
        num2 = int(com[1])
        stack.append(num2)


