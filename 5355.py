import sys
case= int(input())

for i in range(case):
    x = sys.stdin.readline().rstrip().split()
    sum =float(x[0])
    for k in x:
        if k == '@':
            sum *= 3
        elif k == '%':
            sum += 5
        elif k == '#':
            sum -= 7
    print(format(sum, ".2f"))


