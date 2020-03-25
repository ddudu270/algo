import sys
"""
def soin(case):
    sum2= []
    for i in range(2, case):
        if case % i == 0:
            sum2.append(i)
            case = int(case/i)
            soin(case)
        else:
            continue
    print(sum2)

case= int(sys.stdin.readline())
soin(case)

case= int(sys.stdin.readline())
i=2
while case!=1:
    if case%i == 0:
        case=case/i
        print(i)
    else:
        i +=1

list = []
n = 2
while case != 1:
    if case % n ==0:
        case = case / n
        list.append(n)
        n=2
    else:
        n +=1
for i in list:
    print(i)
# 리스트를 또 for문에 넣고 출력해야 해서 두번 고생하는 짓.
"""

case= int(sys.stdin.readline())

while case!=1:
    for i in range(2, case+1):
        if case % i ==0:
            print(i)
            case = case // i
            break




