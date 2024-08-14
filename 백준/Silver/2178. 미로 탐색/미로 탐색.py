import sys
from collections import deque

def bfs(maze_ls, x, y):
    # 현재 노드 방문
    queue = deque([(x, y)])  # 시작 위치 큐에 넣음
    visited_ls[x][y] = True
    distance_ls[x][y] = 1  # 시작점의 거리를 1로 설정
    
    while queue:
        current_x, current_y = queue.popleft()
        
        # 도착 지점(n, m)에 도달한 경우 종료
        if current_x == n-1 and current_y == m-1:
            return distance_ls[current_x][current_y]
        
        for direction in direction_ls:
            # 인접한 칸 중에서
            next_x = current_x + direction[0]
            next_y = current_y + direction[1]
            if 0 <= next_x < n and 0 <= next_y < m:
                # 미로 내에 있고
                if maze_ls[next_x][next_y] == 1 and not visited_ls[next_x][next_y]:
                    # 아직 방문하지 않은 이동할 수 있는 칸인 경우 -> 방문
                    visited_ls[next_x][next_y] = True
                    distance_ls[next_x][next_y] = distance_ls[current_x][current_y] + 1  # 거리 계산
                    queue.append((next_x, next_y)) # 큐에 넣음(방문 예정)
    return
n, m = map(int, sys.stdin.readline().split())
maze_ls = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
distance_ls = [[0] * m for _ in range(n)]  # 각 지점까지의 거리 저장
visited_ls = [[False] * m for _ in range(n)]  # 방문 여부 저장
direction_ls = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 방향
result = bfs(maze_ls, 0, 0)  # (1,1)에서 출발함
print(result)