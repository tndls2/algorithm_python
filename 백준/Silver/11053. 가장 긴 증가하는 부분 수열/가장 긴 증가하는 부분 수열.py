## 최장 증가 부분 수열(LIS, Longest Increasing Subsequence) 문제 

import sys
n = int(input())
sequence_ls = list(map(int, sys.stdin.readline().split()))
dp = [1] * n # 첫 번째 요소 ~ 각 i번째 요소까지에 대해서 최장부분수열의 길이 : 1로 기본 세팅
for i in range(1, n):
    for j in range(i):
        if sequence_ls[j] < sequence_ls[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))  # n번째 요소까지수의 수열에 대한 최장부분수열의 길이 출력
