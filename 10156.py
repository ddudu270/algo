import sys

k, n, m = map(int, sys.stdin.readline().rstrip().split())

if k*n <= m:
    print(0)
else:
    print(k*n-m)