# import sys
#
# num = int(sys.stdin.readline().rstrip())
# queue = []
#
# for i in range(num):
#     list= sys.stdin.readline().rstrip().split()
#     if list[0] == 'push':
#         queue.append(list[1])
#     elif list[0] == 'pop':
#         if queue != []:
#             print(queue.pop(0))
#         else:g
#             print(-1)
#     elif list[0] == 'front':
#         if queue == []:
#             print(-1)
#         else:
#             print(queue[0])
#     elif list[0] == 'back':
#         if queue == []:
#             print(-1)
#         else:
#             print(queue[-1])
#     elif list[0] == 'size':
#         print(len(queue))
#     elif list[0] == 'empty':
#         if queue:
#             print(0)
#         else:
#             print(1)

import sys
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    x, *a = input().split()
    if x == 'push':
        q.append(a[0])
    elif x == 'pop':
        print(q.pop(0) if q else -1)
    elif x == 'size':
        print(len(q))
    elif x == 'empty':
        print(0 if q else 1)
    elif x == 'front':
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)

