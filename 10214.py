import sys

t = int(sys.stdin.readline().rstrip())
sum1 = 0
sum2 = 0

for i in range(t):
    for i in range(9):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        sum1 += x
        sum2 += y
    if sum1 > sum2: print("Yonsei")
    elif sum1 == sum2: print("Draw")
    else: print("Korea")
