import sys

x1, y1 = map(int, sys.stdin.readline().rstrip().split())
x2, y2 = map(int, sys.stdin.readline().rstrip().split())
x3, y3 = map(int, sys.stdin.readline().rstrip().split())

a= [x1, x2, x3]
b= [y1, y2, y3]

a.sort()
b.sort()

if a[0] != a[1]:
    x4= a[0]
else:
    x4= a[2]

if b[0] != b[1]:
    y4= b[0]
else:
    y4= b[2]

print(x4, y4)
