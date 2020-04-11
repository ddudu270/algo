import sys

num = int(sys.stdin.readline().rstrip())

for i in range(num):
    list = sys.stdin.readline().rstrip().split()
    list2 = []
    for j in range(len(list)):
        list2.append(list[j][::-1])
    print(' '.join(list2))
