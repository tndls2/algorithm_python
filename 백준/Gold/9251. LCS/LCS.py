## 블로그 참조하여 해결함 (https://10000cow.tistory.com/entry/%ED%95%9C-%EC%82%B4%EB%8F%84-%EC%9D%B4%ED%95%B4%ED%95%98%EB%8A%94-%EB%B0%B1%EC%A4%80-9251%EB%B2%88-LCS-DPPython)
import sys
first_string = sys.stdin.readline().rstrip()
second_string = sys.stdin.readline().rstrip()

n = len(first_string)  # 첫번째 문자열의 길이
m = len(second_string)  # 두번째 문자열의 길이
dp = [[0] * (m+1) for _ in range(n+1)]  # 두 문자열 간 LCS 길이 저장
# d[i][j]일 때 i=0, j=0은 계산을 위한 값임 (실제 LCS 계산: i>=1, j=>=1)
# i = 세로 인덱스 = 두 번째 문자열의 길이, j = 가로 인덱스 = 첫 번째 문자열의 길이 

for i in range(1, n+1):
    for j in range(1, m+1):
        if first_string[i-1] == second_string[j-1]:
            # 동일한 문자를 찾은 경우
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 서로 다른 문자를 찾은 경우
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[n][m])