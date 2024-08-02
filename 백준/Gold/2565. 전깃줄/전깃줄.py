n = int(input())
pole_ls = [tuple(map(int, input().split())) for _ in range(n)]  # 튜플 성능이 더 좋음

pole_ls.sort()  # A 전봇대 순서: 오름차순 정렬
# 정렬하지 않고 입력된 순서대로 해서 계산하면 복잡해짐
## 1) A 전봇대 순서가 이전이면서 B 전봇대 순서도 이전인 경우
## 2) A 전봇대 순서가 이전이지만 B 전봇대 순서는 이후인 경우
## 3) A 전봇대 순서가 이후이면서 B 전봇대 순서도 이후인 경우
## 4) A 전봇대 순서가 이후이지만 B 전봇대 순서는 이전인 경우
## 각 경우에 또 조건 검사가 더 이루어져서 로직이 복잡해짐

b_positions = [pole_ls[1] for pole_ls in pole_ls]  # B 전봇대 위치(순서 섞임, A 전봇대 순서 반영)

dp = [1] * n  # A 전봇대의 각 자리별로 최대 전깃줄 수
for i in range(1, n):
    for j in range(i):
        if b_positions[j] < b_positions[i]:
            # A 전봇대의 순서가 이전이면서, B전봇대의 순서도 이전인 경우
            dp[i] = max(dp[i], dp[j] + 1)
print(n-max(dp))  # 제거해야하는 전깃줄의 갯수