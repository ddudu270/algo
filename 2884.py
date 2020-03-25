import sys

b = int(sys.stdin.readline().rstrip())
a = list(sys.stdin.readline().rstrip())


for i in range(b):
    sum = a.count('A')
    sum1 = a.count('B')

if sum > sum1:
    print('A')
elif sum < sum1:
    print('B')
else:
    print('Tie')
    

