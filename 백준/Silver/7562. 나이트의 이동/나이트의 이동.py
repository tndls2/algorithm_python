import sys
from collections import deque
def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])  # 시작 위치 큐에 넣음
    distance_ls[start_x][start_y] = 1  # 첫번째 칸 방문 표시
    
    while queue:
        current_x, current_y = queue.popleft()        
        
        # 도달 위치에 도달한 경우 종료
        if (current_x, current_y) == (arrive_x, arrive_y):
            return distance_ls[current_x][current_y] - 1 # 해당 위치 방문 순서 반환 (첫번째 칸 방문은 뺌)
        
        for direction in direction_ls:
            # 이동 가능한 위치 중
            next_x = current_x + direction[0]
            next_y = current_y + direction[1]
            if 0 <= next_x < l and  0 <= next_y < l:
                # 체스판 범위 내에 있고
                if not distance_ls[next_x][next_y]:
                    # 아직 방문하지 않은 경우 (= 방문 순서가 0인 경우) -> 방문
                    distance_ls[next_x][next_y] = distance_ls[current_x][current_y] + 1
                    queue.append((next_x, next_y))
                
    
t = int(input())
direction_ls = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]  # 나이트가 이동할 수 있는 방향

for _ in range(t):
    l = int(input())
    start_x, start_y = map(int, sys.stdin.readline().split())  # 시작 위치 
    arrive_x, arrive_y = map(int, sys.stdin.readline().split())  # 도달 위치
    
    distance_ls = [[0] * l for _ in range(l)]  # 각 칸별 방문 순서
    
    result = bfs(start_x, start_y)  # 시작 위치에서 탐색 시작
    print(result)