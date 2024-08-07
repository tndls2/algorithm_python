import sys

n, k = map(int, sys.stdin.readline().split())
coin_ls = [int(sys.stdin.readline().rstrip()) for _ in range(n)]  # 오름차순으로 입력되어 따로 정렬 필요 없음
answer = 0

for i in range(n-1, -1, -1):  # 동전의 갯수를 최소로 하기 위해 가치가 가장 큰 동전부터 순회
    cnt = k // coin_ls[i]  # 해당 동전으로 k원을 만들 수 있는 경우
    if cnt > 0:
        answer += cnt  # 필요한 동전 갯수 카운트
        k -= coin_ls[i] * cnt
    if k == 0:
        break  # k가 0이 되면 종료

print(answer)
