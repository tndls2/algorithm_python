import sys

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if dp[a][b][c]:  # dp에 저장되어 있으면 해당 값 리턴
        return dp[a][b][c]
    
    # dp에 저장되어 있지 않다면 저장하기
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]  # 값을 기억해놓을 배열 선언 (범위: 0~20)
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')