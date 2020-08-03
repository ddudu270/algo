import sys


def DFS(x):
    if x == m:  # 수열 m개를 충족할경우 출력
        print(*array)
        return

    for i in range(n):
        if check_number[i]:  # 중복될 경우 패스
            continue

        array.append(number_list[i])  # 수열 추가
        check_number[i] = True  # 사용한 수 체크

        DFS(x + 1)  # + 1번째 수열을 위해 재귀함수 호출

        array.pop()  # 수열 마지막 자리 삭제
        check_number[i] = False  # 사용한 수 초기화


n, m = map(int, sys.stdin.readline().split())

number_list = [i + 1 for i in range(n)]  # 숫자 리스트
check_number = [False] * n  # 방문 체크
array = []  # 출력할 수열

DFS(0)
