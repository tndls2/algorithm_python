## 블로그 참조하여 해결함
import sys
def find_fill_chess(prefix_color):
    fill_sum_ls = [[0] * (m + 1) for _ in range(n + 1)]  # 각 칸 별 색칠 횟수 누적합 저장
    #
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i + j) % 2 == 0:  
                # prefix_color가 칠해져 있어야 하는 칸
                value = 1 if board_ls[i - 1][j - 1] != prefix_color else 0  # 색이 다르면 색을 칠해야 함
            else:  
                # prefix_color가 아닌 색이 칠해져 있어야 하는 칸
                value = 0 if board_ls[i - 1][j - 1] != prefix_color else 1  # 색이 다르면 색을 칠해야 함
            # 2차원 배열의 누적합 구하기
            fill_sum_ls[i][j] = value + fill_sum_ls[i - 1][j] + fill_sum_ls[i][j - 1] - fill_sum_ls[i - 1][j - 1]
    
    min_fill = float('inf')  # 파이썬에서 가장 큰 값
    
    # 각 칸 별 누적합을 이용해서 원하는 구간의 합 구하기
    for i in range(k, n + 1):
        for j in range(k, m + 1):
            # 2차원 배열의 구간합 구하기 (합집합을 고려해야 함)
            # 참조 : https://jih3508.tistory.com/50
            total_fill = fill_sum_ls[i][j] - fill_sum_ls[i - k][j] - fill_sum_ls[i][j - k] + fill_sum_ls[i - k][j - k]
            min_fill = min(min_fill, total_fill)
    return min_fill

# n, m, k 입력받기
n, m, k = map(int, sys.stdin.readline().split())
# board_ls를 이중 배열로 입력받기
board_ls = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# 검은색 칸으로 시작하는 체스판, 흰색 칸으로 시작하는 체스판으로 색칠하는 경우 중 가장 최소비용이 드는 방법으로 선택
answer = min(find_fill_chess('B'), find_fill_chess('W'))
print(answer)