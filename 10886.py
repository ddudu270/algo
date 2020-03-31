import sys

num = int(sys.stdin.readline().rstrip())
sum =0

for i in range(num):
    n = int(sys.stdin.readline().rstrip())
    sum += n

if sum < num/2:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
