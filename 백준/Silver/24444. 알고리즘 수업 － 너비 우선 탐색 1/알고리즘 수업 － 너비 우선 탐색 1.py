import sys
from collections import deque
sys.setrecursionlimit(150000)

def bfs(graph, v, visited, order):
    queue = deque([v]) # 시작 노드를 큐에 넣음
    visited[v] = True
    cnt = 1
    order[v] = cnt
    
    while queue:
        current_v = queue.popleft()  # 현재 노드에 대해
        for next_v in graph[current_v]:  # 인접한 노드들 중
            if not visited[next_v]:  # 방문하지 않은 노드 -> 방문
                visited[next_v] = True
                cnt += 1
                order[next_v] = cnt
                queue.append(next_v)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)] # 각 노드별 인접 노드 저장

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    # 무방향 그래프
    graph[x].append(y)
    graph[y].append(x)

# 각 노드별 인접노드 -> 오름차순 정렬
for i in range(1, n+1):
    graph[i].sort()

order = [0] * (n+1)  # 각 노드별 방문 순서 저장
visited = [False] * (n+1)  # 각 노드별 방문 여부 저장

bfs(graph, r, visited, order)

for i in range(1, n+1):
    print(order[i])
