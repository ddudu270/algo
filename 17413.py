import sys

list = sys.stdin.readline().rstrip()
stack = []
sum = ''
tag = False

for i in list:
    if i == '<':
        while stack: # 스택에 존재할 때
            sum += stack.pop()
        sum += i
        tag = True
    elif i == '>':
        sum += i
        tag = False
    elif tag:
        sum += i
    elif i == ' ':
        while stack: # 스택에 존재할 때
            sum += stack.pop()
        sum += i
    else:
        stack.append(i)
while stack:
    sum += stack.pop()
print(sum)


