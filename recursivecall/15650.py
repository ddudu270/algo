import sys


def dfs(x):
    if x == M:  # 필요한 자릿수가 다 차면 출력
        print(*arr)
        return

    for i in range(N):  # 숫자를 키우는 단계
        if visit[i]:  # 중복일 경우 i를 한단계 증가
            continue

        arr.append(num_list[i])
        # 이미 앞은 나왔고 그 다음 숫자를 더하는 과정
        visit[i] = True

        dfs(x + 1)  # 예를 들어 2 4라면 그 다음 숫자를 위해 또 dfs를 실행

        arr.pop()
        for j in range(i+1, N):
            visit[j] = False


N, M = map(int, sys.stdin.readline().split())
num_list = [i + 1 for i in range(N)]  # 숫자 리스트
visit = [False] * N  # 방문 체크
arr = []  # 출력할 리스트

dfs(0)
