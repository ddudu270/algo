import sys

x,y,z= map(int, sys.stdin.readline().rstrip().split())
yum= int(sys.stdin.readline().rstrip())

sea= int(yum/3600)
boon= int((yum-(sea*3600))/60)
cho= (yum-(sea*3600))%60

hour2 = x+sea
min2 = y+boon
sec2= z+cho

if sec2 >=60:
    min2 += 1
    sec2 -= 60

if min2 >= 60:
    hour2 += 1
    min2 -= 60

if hour2 >= 24:
    hour3 = int(hour2/24)
    hour2 = hour2-(hour3*24)

print(hour2, min2, sec2)