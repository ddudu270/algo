import sys

a = list(sys.stdin.readline().rstrip())
sum = 10

for i in range(len(a)-1):
    if a[i] == '(':
        if a[i + 1] == '(':
            sum += 5
        else:
            sum += 10
    if a[i] == ')':
        if a[i + 1] == ')':
            sum += 5
        else:
            sum += 10

print(sum)

# numbers = ['one', 'two', 'three', 'four', 'five']
#
# for n in numbers:
#     print(n)
