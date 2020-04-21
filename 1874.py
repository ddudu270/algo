import sys

num = int(sys.stdin.readline())

just = []
list = []
result = []
idx = 0

for j in range(num):
    just.append(int(sys.stdin.readline()))

for i in range(num):
    list.append(i + 1)
    result.append("+")

    while idx < num and len(list) != 0 and list[-1] == just[idx]:
        list.pop()
        result.append("-")
        idx += 1

if list:
    print("NO")
else:
    for i in result:
        print(i)
