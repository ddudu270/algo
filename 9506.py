import sys

while True:
    list2 = []
    num = int(sys.stdin.readline().rstrip())
    if num == -1:
        break
    else:
        for i in range(1, num):
            if num % i == 0:
                list2.append(i)
            else:
                continue
        if sum(list2) == num:
            a = list(map(str, list2))
            b = ' + '.join(a)
            print(num,"=",b)
        else:
            print(num,"is NOT perfect.")