from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()

        print(v, end=' ')

        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
