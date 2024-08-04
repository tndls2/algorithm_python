n, k = map(int, input().split())  # n, k 입력
weight_values = [tuple(map(int, input().split())) for _ in range(n)]  # weight, value 입력
weight_ls = [weight for weight, value in weight_values]  # weight만 분리
values_ls = [value for weight, value in weight_values]  # value만 분리

dp = list([0]* (k + 1) for _ in range(n + 1))  # dp[i][j] = i번째 물건까지 있고 jkg까지 무게를 담을 수 있을 때, 가질 수 있는 최대 value값 저장

# bottom-up 방식으로 구함
# 방법론 참조 : https://www.youtube.com/watch?v=rhda6lR5kyQ
for i in range(1, n+1):
    for j in range(1, k+1):
        if weight_ls[i - 1] <= j:
            # 현재 물건을 담을 수 있는 경우
            # -> 포함 유무에 따른 value가 더 큰 경우를 선택
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight_ls[i - 1]] + values_ls[i - 1])
        else:
            # 현재 물건을 담을 수 없는 경우
            dp[i][j] = dp[i - 1][j]

            
print(dp[n][k])