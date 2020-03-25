import sys

x,y,z = map(int, sys.stdin.readline().rstrip().split())

if x >= y and x >= z:
    if y>=z:
        print(y)
    else: print(z)
elif y >= x and y >= z:
    if x>=z:
        print(x)
    else: print(z)
elif z >= x and z >= y:
    if x>=y:
        print(x)
    else: print(y)

# 아주 어리석은 풀이. sort쓰면 바로 해결...