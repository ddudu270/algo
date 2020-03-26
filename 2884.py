import sys

h, m = map(int, sys.stdin.readline().rstrip().split())

if m >= 45:
    h1 = h
    m1 = m - 45
elif m < 45 and h > 0:  # m이 45보다 작으면서 h가 0 아님
    h1 = h - 1
    m1 = 15 + m
else:  # m이 45보다는 작은데 h가 0이라서 h1이 23이 될때
    h1 = 23
    m1 = 15 + m

print(h1, m1) # 바로 출력도 가능
