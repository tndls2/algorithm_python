## 최장 증가 부분 수열(LIS, Longest Increasing Subsequence) 응용 문제
## 다른 코드 참조
import sys
n = int(input())
sequence_ls = list(map(int, sys.stdin.readline().split()))  # 수열 S
dp = [1] * n  # LIS 계산할 리스트
dp_reverse = [1] * n  # 마지막 요소부터 LIS 계산할 리스트

# 첫 번째 요소부터 LIS 계산
for i in range(1, n):
    for j in range(i):
        if sequence_ls[j] < sequence_ls[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 마지막 요소부터 LIS 계산
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if sequence_ls[j] < sequence_ls[i]:
            dp_reverse[i] = max(dp_reverse[i], dp_reverse[j] + 1)


# 바이토닉 수열의 최대 길이 계산
max_length = 0
for i in range(n):
    max_length = max(max_length, dp[i] + dp_reverse[i] - 1)

print(max_length)