import sys


def dfs(x):
    if x == M:  # 자릿수 확인
        print(*arr)
        return

    # 여기는 중복 확인을 안 해도 됨
    for i in range(N):
        arr.append(num_list[i])
        # 방문 체크

        dfs(x + 1)

        arr.pop()


N, M = map(int, sys.stdin.readline().split())
num_list = [i + 1 for i in range(N)]
visit = [False] * N
arr = []

dfs(0)
