import sys

case = int(input())
sum= ''

for i in range(case):
    x,y = map(str, sys.stdin.readline().rstrip().split())
    z= int(x)
    for j in y:
        sum = sum + j*z
    print(sum)
    sum=''
