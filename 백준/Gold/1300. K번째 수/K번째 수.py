import sys


def binary_search(target, start, end):
    global result
    count = 0
    if start > end:
        return
    mid = (start + end) // 2

    for i in range(1, n + 1):
        count += min(mid // i, n)

    if count < target:
        # 원하는 인덱스 미만 경우 -> 더 큰 값에서 탐색
        binary_search(target, mid + 1, end)
    else:
        # 원하는 인덱스 이상인 경우 -> 더 작은 값에서 탐색
        result = mid  # 일단 값 저장
        binary_search(target, start, mid - 1)


n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())  # 찾아야하는 원소의 오름차순 순서
ls = []
result = 0

binary_search(k, 1, n * n)
print(result)
