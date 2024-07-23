## 다른 코드들 참고해서 해결함 ##
import sys

def binary_search(start, end):
    global result  # 전역변수 설정
    if start > end:
        return

    mid = (start + end) // 2
    count = sum(lan // mid for lan in lan_ls)  # 만들 수 있는 랜선 갯수

    if count >= n:  
        # 1. 랜선 갯수가 n개인 경우 -> 최대 길이까지 길이 늘리기
        # 2. 랜선 갯수가 n을 초과하는 경우 -> 길이를 늘려서 랜선 갯수 줄이기
        result = mid  # 일단 현재 랜전 길이 저장
        binary_search(mid + 1, end)  # 탐색
    else:  
        # 랜선 갯수가 n 미만인 경우 -> 길이를 줄여서 갯수 늘리기
        binary_search(start, mid - 1)  # 탐색

# 입력 받기
k, n = map(int, sys.stdin.readline().split())
lan_ls = [int(sys.stdin.readline().rstrip()) for _ in range(k)]
result = 0

# 이진 탐색을 위한 초기값 설정
start = 1
end = max(lan_ls)

binary_search(start, end)  # 이진 탐색
print(result)