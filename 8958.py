import sys

num = int(sys.stdin.readline().rstrip())

for i in range(num):
    list = sys.stdin.readline().rstrip()
    sum = 0
    sum2 = 0
    for j in list:
        if j == 'O':
            sum += 1 # sum에 1씩 계속 더해줘야 함
            sum2 += sum # 그 sum을 sum2에 계속 더해놔야 함
        else:
            sum = 0 # x를 만나면 sum을 다 초기화
            sum2 += sum #그러면 sum을 더해도 어차피 0을 더하는 것
            # 그러다 O를 다시 만나도 어차피 sum에는 1이 또 더해짐
    print(sum2)
