import sys

num = int(sys.stdin.readline())
deque = []

for i in range(num):
    list = sys.stdin.readline().rstrip().split()
    if list[0] == 'size':
        print(len(deque))
    elif list[0] == 'empty':
        print(0 if deque else 1)
    elif list[0] == 'front':
        print(deque[0] if deque else -1)
    elif list[0] == 'back':
        print(deque[-1] if deque else -1)
    elif list[0] == 'push_back':
        deque.append(int(list[1]))
    elif list[0] == 'push_front':
        deque.insert(0, int(list[1]))
    elif list[0] == 'pop_front':
        print(deque.pop(0) if deque else -1)
    elif list[0] == 'pop_back':
        print(deque.pop(-1) if deque else -1)
