import sys

num = int(sys.stdin.readline().rstrip())
stack = []

for i in range(num):
    com = sys.stdin.readline().rstrip()
    flag = True
    if com.count('(') == com.count(')'):
        for j in range(len(com)):
            if com[j] == "(":
                stack.append(com[j])
            else:
                if stack:
                    stack.pop()
                else:
                    flag = False
                    break
        if flag:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
