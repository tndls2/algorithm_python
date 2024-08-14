import sys
sys.setrecursionlimit(10 ** 6)

def dfs(fields, row, col, visited):
    global direction_ls
    # 현재 노드 방문
    visited[row][col] = True
    
    for direction in direction_ls:
        # 인접한 밭에 대해서
        next_row = row + direction[0]
        next_col = col + direction[1]
        
        if 0 <= next_row < m and 0 <= next_col < n:
            # 밭의 범위 안에 있고
            if not visited[next_row][next_col] and fields[next_row][next_col]:
                # 아직 방문하지 않은 배추 심은 위치인 경우 -> 방문
                dfs(fields, next_row, next_col, visited)

t = int(input())
direction_ls = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 방향
for _ in range(t):
    m, n, k = map(int, input().split())
    
    fields = [[0] * n for _ in range(m)]  # 기본적으로 0 설정
    visited = [[False] * n for _ in range(m)]  # 방문 여부 체크
    
    for _ in range(k):
        # 배추 위치 표시 (1 설정)
        x, y = map(int, sys.stdin.readline().strip().split())
        fields[x][y] = 1

    cnt = 0  # 배추가 심어진 영역의 수
    
    # 배추밭 탐색
    for i in range(m):
        for j in range(n):
            if fields[i][j] == 1 and not visited[i][j]:
                # 아직 방문하지 않은 배추 위치
                dfs(fields, i, j, visited)
                cnt += 1  # 새로운 배추 영역 발견 시 카운트
    
    print(cnt)
