import sys
sys.setrecursionlimit(10 ** 6)

def dfs(graph, v, visited, order, cnt):
    visited[v] = True
    order[v] = cnt
    
    for i in graph[v]:
        # 인접한 노드 중
        if not visited[i]:  # 아직 방문하지 않은 노드 방문
            cnt = dfs(graph, i, visited, order, cnt + 1)
    
    return cnt

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    # 무방향 그래프
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort(reverse=True)  # 내림차순 정렬

order = [0] * (n+1)  # 각 노드별 방문 순서 저장
visited = [False] * (n+1)  # 각 노드별 방문 여부 저장

dfs(graph, r, visited, order, 1)  # 첫번째 방문 시작

for i in range(1, n+1):
    print(order[i])
