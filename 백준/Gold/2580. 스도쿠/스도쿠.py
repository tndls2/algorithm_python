## 다른 코드들 참고해서 해결함 ##

import sys

def check_row(row, num):
    # 같은 행 체크
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    return True

def check_column(column, num):
    # 같은 열 체크
    for i in range(9):
        if sudoku[i][column] == num:
            return False
    return True

def check_square(row, column, num):
    # 3*3 스도쿠 체크
    start_row = (row // 3) * 3
    start_column = (column // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_column + j] == num:
                return False
    return True

def fill_blank(n):
    global sudoku, blank
    
    if n == len(blank):
        return True  # 모든 빈칸을 채운 경우
    
    row, column = blank[n]
    
    for num in range(1, 10):
        if check_row(row, num) and check_column(column, num) and check_square(row, column, num):
            # 빈칸 채우기
            sudoku[row][column] = num
            
            if fill_blank(n + 1):  # 다음 빈칸에 대해 탐색
                return True
            
            sudoku[row][column] = 0  # 백트래킹을 위해 다시 빈 칸으로 복구
    
    return False

# 입력 받기
sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = []  # 빈칸 위치 저장
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))

# 빈 칸 채우기
fill_blank(0)

# 결과 출력
for row in sudoku:
    print(" ".join(map(str, row)))
