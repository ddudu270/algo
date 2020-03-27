import sys

while True:
    m, f = map(int, sys.stdin.readline().rstrip().split())
    if m == 0 and f ==0:
        break
    else:
        print(m+f)
