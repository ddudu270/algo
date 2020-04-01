import sys


def palindrome(p):
    for i in range(len(p) // 2):
        if p[i] == p[-1 - i]:
            continue
        else:
            return 0
    return 1


p = list(sys.stdin.readline().rstrip())
x=palindrome(p)
print(x)

# from sys import stdin
#
# t = stdin.readline().strip()
# if t == t[::-1]:
#     print(1)
# else:
#     print(0)
