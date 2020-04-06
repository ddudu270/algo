import sys

num = int(sys.stdin.readline().rstrip())

for i in range(num):
    k = int(sys.stdin.readline().rstrip())
    m = ''
    n = 0
    for j in range(k):
        x, y = sys.stdin.readline().rstrip().split()
        if int(y) > n:
            n = int(y)
            m = x
    print(m)
