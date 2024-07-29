dp = [1, 1, 1]  # 미리 값을 저장할 배열 선언

def padovan_sequence(n):
    if n > len(dp):
        for i in range(len(dp), n):
            dp.append(dp[i - 3] + dp[i - 2])
    return dp[n - 1]  # dp의 인덱스는 0부터 시작함 -> P[3] = dp[2]

n = int(input())  # 첫 번째 입력: 테스트 케이스 수
for _ in range(n):
    m = int(input())  # 각 테스트 케이스 입력
    result = padovan_sequence(m)
    print(result)
