import sys
from _collections import deque


def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        for e in graph[v]:
            if not visited[e]:
                visited[e] = True
                q.append(e)


n, m = map(int, sys.stdin.readline().split())
# n = 정점의 개수, m = 간선의 개수
graph = [[] for _ in range(n + 1)]
count = 0

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)

for e in range(1, n + 1):
    if not visited[e]:  # visit을 하지 않은 상태라면
        count += 1
        bfs(e)

print(count)
