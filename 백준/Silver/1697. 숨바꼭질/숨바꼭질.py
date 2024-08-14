import sys
from collections import deque
def bfs(start):
    queue = deque([start])  # 시작 위치 큐에 넣음
    
    while queue:
        current_pos = queue.popleft()        
        
        # 동생 위치에 도달한 경우 종료
        if current_pos == k:
            return time_ls[current_pos]  # 해당 위치까지 도달하는데 걸린 시간 반환
        
        next_pos_ls = [current_pos - 1, current_pos + 1, current_pos * 2]  # 1초 동안 갈 수 있는 위치
        for next_pos in next_pos_ls:
            if 0 <= next_pos <= max_distance and not time_ls[next_pos]:
                # 해당 위치가 아직 방문하지 않았으며, 갈 수 있는 범위인 경우
                time_ls[next_pos] = time_ls[current_pos] + 1
                queue.append(next_pos)
                
n, k = map(int, sys.stdin.readline().split())
max_distance = 10**5
time_ls = [0] * (max_distance + 1)

result = bfs(n)  # 현재 위치에서 탐색 시작

print(result)