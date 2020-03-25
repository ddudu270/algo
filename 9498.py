import sys

case = int(sys.stdin.readline())

if case >= 90:
    print('A')
elif 80 <= case and case <= 89:
    print('B')
elif 70 <= case and case <= 79:
    print('C')
elif 60 <= case and case <= 69:
    print('D')
else:
    print('F')

