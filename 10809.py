import sys

alpha = [-1 for i in range(26)]

list = sys.stdin.readline().rstrip()

for i in list:
    alpha[ord(i) - ord('a')] = list.find(i)

for i in alpha:
    print(i, end=' ')

