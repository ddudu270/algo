import sys

while True:
    one, two, three, four = 0, 0, 0, 0
    list2 = sys.stdin.readline().rstrip('\n')

    if not list2:
        break
    for j in list2:
        if 97 <= ord(j) and ord(j) <= 122:
            one += 1
        elif 65 <= ord(j) and ord(j) <= 90:
            two += 1
        elif 48 <= ord(j) and ord(j) <= 57:
            three += 1
        elif ord(j) == 32:
            four += 1
    print(one, two, three, four)
