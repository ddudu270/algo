"""
import sys

won = int(sys.stdin.readline())
se = int(sys.stdin.readline())
sang = int(sys.stdin.readline())
sung = int(sys.stdin.readline())
kang = int(sys.stdin.readline())

if won < 40:
    won = 40
if se < 40:
    se = 40
if sang < 40:
    sang = 40
if sung < 40:
    sung = 40
if kang < 40:
    kang = 40

print(int((won+se+sang+sung+kang)/5))
"""
sum =0
for i in range(5):
    score= int (input())
    if score < 40:
        score= 40
    sum += score

print(sum // 5)