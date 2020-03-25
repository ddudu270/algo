import sys

x= int(sys.stdin.readline())
y = sys.stdin.readline().rstrip()
z = int(sys.stdin.readline())

if y == '*':
    print(x*z)
else:
    print(x+z)
