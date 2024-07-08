## 다른 코드들 참고하여 해결함 ##

def dfs(row):
    global n, answer, cols, diag_left, diag_right  # 전역변수 설정
    if row == n:
        # 모든 행에 대한 순회가 완료된 경우
        answer += 1
        return
    for col in range(n):
        if cols[col] or diag_left[row - col] or diag_right[row + col]:
            continue  # 이미 해당 열 또는 대각선에 퀸이 있으면 skip
        # 현재 위치에 퀸을 놓음
        cols[col] = diag_left[row - col] = diag_right[row + col] = True
        dfs(row + 1)  # 다음 열에 대해 탐색
        
        # 백트래킹을 위해 퀸을 다시 제거
        cols[col] = diag_left[row - col] = diag_right[row + col] = False
n = int(input())
answer = 0  # 경우의 수
cols = [False] * n  # cols[i]: i번째 열에 Queen이 있는지 여부
diag_left = [False] * (2 * n - 1)  # diag1[i]: 왼쪽 대각선에 Queen이 있는지 여부
diag_right = [False] * (2 * n - 1)  # diag2[i]: 오른쪽 대각선에 Queen이 있는지 여부
dfs(0) # 첫번째 열에 Queen을 놓음
print(answer)