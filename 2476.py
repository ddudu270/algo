import sys

num = int(sys.stdin.readline())
sum = 0

for i in range(num):
    a, b, c = sorted(map(int, sys.stdin.readline().rstrip().split()))
    if a == c:
        sum0 = 10000 + a * 1000
    elif a!=b and b!=c:
        sum0 = c*100
    else:
        sum0 = 1000+ b*100

    if sum0 > sum:
        sum= sum0

print(sum)
