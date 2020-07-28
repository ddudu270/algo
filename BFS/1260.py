import sys


def bfs(graph, root):
    need_visit, visited = list(), list()
    need_visit.append(root)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


def dfs(graph, root):
    need_visit, visited = list(), list()
    need_visit.append(root)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(reversed(graph[node]))

    return visited


n, m, root = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

print(*dfs(graph,root))
print(*bfs(graph,root))
