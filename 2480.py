import sys

# x, y, z = map(int, sys.stdin.readline().rstrip().split())
#
# if x == y and y ==z:
#     sum = 10000 + (x*1000)
# elif x==y :
#     sum = 1000+ x*100
# elif z==y :
#     sum = 1000+ z*100
# elif x==z :
#     sum = 1000+ x*100
# else:
#     sum = max(x,y,z) * 100
#
# print(sum)

# a = list(map(int, input().split()));
# r = 0
# for i in a:
#     k = a.count(i)
#     if k > 1: r = (10 + i)
# if r == 0: r = max(a)
# print(r * 100 * (10 ** (k > 2)))

l = sorted(list(map(int, input().split())))
s = len(set(l))
print(l[s - 1] * [100, 1000][s == 1] + [10000, 1000, 0][s - 1])
