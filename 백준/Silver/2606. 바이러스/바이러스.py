import sys
sys.setrecursionlimit(150000)

def dfs(graph, v, visited, cnt):
    visited[v] = True  # 현재 노드 방문
    
    for i in graph[v]: # 인접한 노드들 중
        if not visited[i]:  # 방문하지 않은 노드 -> 방문
            cnt = dfs(graph, i, visited, cnt + 1)
    
    return cnt

n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 컴퓨터 상 수

graph = [[] for _ in range(n + 1)]  # 각 컴퓨터별 인접 컴퓨터 저장할 배열

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    # 네트워크 = 무방향 그래프
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)  # 각 노드별 방문 여부 저장

answer = dfs(graph, 1, visited, 1)  # 총 바이러스에 걸린 컴퓨터 수

print(answer-1)  # 첫번째 컴퓨터 제외하고 계산해야함
