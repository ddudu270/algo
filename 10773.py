import sys

num = int(sys.stdin.readline())
list = []

for i in range(num):
    data= int(sys.stdin.readline())
    if data == 0 and len(list) > 0:
        list.pop()
    else:
        list.append(data)

print(sum(list))