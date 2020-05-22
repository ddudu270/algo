import sys

list2 = []
sum = 0
sum2 = 0
n, m = map(int, sys.stdin.readline().rstrip().split())

list2 = sys.stdin.readline().rstrip().split()
list2 = list(map(int, list2))

for i in range(0, len(list2)):
    for j in range(i + 1, len(list2)):
        for k in range(j + 1, len(list2)):
            sum2 = list2[i] + list2[j] + list2[k]
            if sum2 <= m and sum2 > sum:
                sum = sum2

print(sum)
