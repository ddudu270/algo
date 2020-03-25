import sys

"""
num = int(sys.stdin.readline())
list1 = []
list2 = []
list3 = []

for j in range(num):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if x == 1:
        list1 = [1]
    while x > 1:
        for i in range(2, x + 1):
            if x % i == 0:
                x = x // i
                list1.append(i)
                break
    if y == 1:
        list2 = [1]
    while y > 1:
        for i in range(2, y + 1):
            if y % i == 0:
                y = y // i
                list2.append(i)
                break

    print(list1)
    print(list2)
"""
num = int(sys.stdin.readline())

for j in range(num):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    gcd = 1
    for k in range(2, min(a, b)+1):
        while (a % k == 0) & (b % k == 0):
            a = a // k
            b = b // k
            gcd = gcd * k
    lcd = gcd * a * b
    print(lcd)
