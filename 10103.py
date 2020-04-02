import sys

num = int(sys.stdin.readline().rstrip())
x2 = 100
y2 = 100

for i in range(num):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if x == y:
        continue
    elif x < y:
        x2 -= y
    else:
        y2 -= x

print(x2, y2)
