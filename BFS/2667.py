import sys
from _collections import deque


def bfs(i, j, count):
    visit[i][j] = count # 방문을 count로 해줘야 나중에 셈이 가능
    q = [[i,j]] # 큐에 지금 좌표를 넣어줌
    grid[i][j] = 0 # 1을 0으로 바꿔버림
    while q: # 이제부터 4방향 탐색 시작
        x,y = q.popleft()



n = int(sys.stdin.readline())
grid = [list(map(int, input())) for _ in range(n)]  # 배열 생성
visit = [[0] * n for _ in range(n)]  # 방문 확인!
count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):  # 노션 1번
    for j in range(n):
        if grid[i][j] == 1 and visit[i][j] == 0:
            count += 1 # 노션 3번
            bfs(i, j, count) # 노션 5번
