import sys

list = sys.stdin.readline().rstrip()
alpha= [0 for i in range(26)]

for i in list:
    alpha[ord(i) - ord('a')] += 1

for i in alpha:
    print(i,end=' ')




