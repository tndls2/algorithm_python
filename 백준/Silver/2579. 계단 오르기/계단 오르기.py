import sys
n = int(input())  # 300 이하의 자연수
ls_score = list(map(int, (sys.stdin.readline().rstrip() for _ in range(n))))
dp = [0] * n  # 각 계단에 도착했을 때 가질 수 있는 최댓값

dp[0] = ls_score[0]  # 첫번째 계단에 도착했을 때 가질 수 있는 최댓값 = 자신의 점수
if n>1:
    dp[1] = dp[0] + ls_score[1]  # 두번째 계단에 도착했을 때 가질 수 있는 최댓값 = 첫번째 계단 점수 + 자신의 점수
if n>2:
    dp[2] = max(dp[0] + ls_score[2], ls_score[1] + ls_score[2])  # 세번째 계단에 도착했을 때 가질 수 있는 최댓값 = (첫번째 계단 점수 + 자신의 점수) or (두번째 계단 점수 + 자신의 점수)

if n > 3:
    for i in range(3,n):
        # dp[i-2] + ls_score[i] : (i-2)번째 계단에서 현재 계단으로 오름
        # dp[i-3]+ls_score[i-1]+ls_score[i] : (i-1)번째 계단에서 현재 계단으로 오름 (연속 3계단 오르는 것은 안된다는 점 고려)
        dp[i] = max(dp[i-2] + ls_score[i], dp[i-3] + ls_score[i-1] + ls_score[i])
        
print(dp[n-1])  # n번째 계단에서 가질 수 있는 최댓값