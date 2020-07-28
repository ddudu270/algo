import sys
from _collections import deque


def bfs(i, j, cnt):
    num = 1
    visit[i][j] = cnt  # 방문을 count로 해줘야 나중에 셈이 가능 (4번)
    q = deque()  # 큐에 지금 좌표를 넣어줌
    q.append((i, j))
    grid[i][j] = 0  # 1을 0으로 바꿔버림
    while q:  # 이제부터 4방향 탐색 시작
        x, y = q.popleft()
        for k in range(4):  # 2번
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:  # 벗어났는지 확인
                if grid[nx][ny] == 1 and visit[nx][ny] == 0:
                    num += 1
                    q.append((nx, ny))
                    visit[nx][ny] = cnt
    return num


n = int(sys.stdin.readline())
grid = [list(map(int, input())) for _ in range(n)]  # 배열 생성
visit = [[0] * n for _ in range(n)]  # 방문 확인!
count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = []

for i in range(n):  # 문제 해결 1번
    for j in range(n):
        if grid[i][j] == 1 and visit[i][j] == 0:
            count += 1  # 3번
            ans.append(bfs(i, j, count))  # 5번

ans.sort()

print(count)
for i in ans:
    print(i)
