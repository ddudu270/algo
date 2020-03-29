import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    r, e, c = map(int, sys.stdin.readline().rstrip().split())
    if r < e-c:
        print("advertise")
    elif r == e-c:
        print("does not matter")
    else:
        print("do not advertise")

