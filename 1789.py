"""
import sys

num = int(sys.stdin.readline())
sum = 0


for i in range(1,num):
    sum += i
    if sum > num:
        break
print(i-1)


while sum < num:
    for i in range(1, num):
        sum = sum + i
        if sum > num:
            break
print(i - 1)


num1= 0
for i in range(1,num):
    sum += i
    if sum > num:
        break
    else: num1 +=1
print(num1)
"""


s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)
