# 블로그 참조하여 해결함
import sys
import itertools

t = int(input())
for _ in range(t):
    file_count = int(input())
    cost_ls = list(map(int, sys.stdin.readline().split()))
    
    cost_sum_ls = [0] + list(itertools.accumulate(cost_ls)) # cost_sum_ls[i] = 첫번재 파일부터 i번째 파일까지의 누적합 저장
    cost_dp = [[0] * file_count for _ in range(file_count)]  # dp[i][j] = i번째 파일 ~ j번째 파일을 합치는 데 드는 최소 비용
    
    # 인접한 두 파일을 합칠 때 드는 비용 계산
    # 두 파일의 크기를 더한 값 -> 테이블에 저장
    for i in range(file_count - 1):
        cost_dp[i][i + 1] = cost_ls[i] + cost_ls[i + 1]

    # 2차원 배열을 전부 탐색하는 것이 아님 
    # cost_dp[i][i]는 해당 파일의 크기임
    # 각 행에서 cost_dp[i][i+1]부터 탐색하며 계산
    for length in range(2, file_count + 1):  # 합치려는 파일의 크기가 작은 것부터 계산 (2개 ~)
        for i in range(file_count - length + 1):
            j = i + length - 1 
            cost_dp[i][j] = sys.maxsize
            total_cost = cost_sum_ls[j+1] - cost_sum_ls[i]  # i번째 파일 ~ j번째 파일 부분합 더하기
            for k in range(j-i):  # 파일을 합치는 모든 조합에 대해서 계산하여 최솟값 구하기
                cost_dp[i][j] = min(cost_dp[i][j], cost_dp[i][i+k] + cost_dp[i+k+1][j] + total_cost)
            
    print(cost_dp[0][file_count-1])  # 첫번째 파일부터 마지막 파일까지 합치는 데 드는 최소 비용
