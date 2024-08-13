import sys
sys.setrecursionlimit(150000)

def dfs(map_ls, row, col, visited):
    visited[row][col] = True  # 현재 노드 방문
    cnt = 1  # 현재 집을 포함하여 카운트 시작

    for direction in direction_ls:
        next_row = row + direction[0]
        next_col = col + direction[1]
        if 0 <= next_row < n and 0 <= next_col < n:
            # 지도 범위 안에 있고
            if map_ls[next_row][next_col] == 1 and not visited[next_row][next_col]:
                # 아직 방문하지 않은 집이라면
                cnt += dfs(map_ls, next_row, next_col, visited)
    return cnt

n = int(input())  # 지도 크기
map_ls = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]  # 지도 입력받기
visited = [[False] * n for _ in range(n)]  # 각 칸별 방문 여부 저장
complex_ls = []  # 단지별 집의 수 저장
direction_ls = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 방향

for i in range(n):
    for j in range(n):
        if map_ls[i][j] == 1 and not visited[i][j]:
            # 아직 방문하지 않은 집인 경우
            complex_ls.append(dfs(map_ls, i, j, visited))

complex_ls.sort()  # 오름차순 정렬

print(len(complex_ls))  # 단지의 수
for count in complex_ls:
    print(count)  # 각 단지의 집 수
