import sys
sys.setrecursionlimit(150000)  # 재귀 깊이 제한을 늘림

def dfs(graph, v, visited, order, cnt):
    visited[v] = True
    order[v] = cnt
    
    for i in graph[v]:
        if not visited[i]:
            cnt = dfs(graph, i, visited, order, cnt+1)
    return cnt

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    # 양방향 간선
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    graph[i].sort()  # 각 노드별 인접 노드 오름차순 정렬

visited = [False] * (n + 1)  # 각 노드별 방문 여부
order = [0] * (n + 1)  # 각 노드의 방문 순서 저장

dfs(graph, r, visited, order, 1)  # 첫 번째 방문 시작

for i in range(1, n + 1):
    print(order[i])
