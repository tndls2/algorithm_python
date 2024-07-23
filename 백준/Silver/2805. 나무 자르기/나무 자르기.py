import sys

def binary_search(start, end):
    global result  # 절단기에 설정한 높이
    if start > end:
        return
    mid = (start + end) // 2  # 절단기에 설정한 높이
    total_tree = sum(tree - mid for tree in tree_ls if tree > mid)  # 가져갈 수 있는 나무 길이
    if total_tree == m:
        # 나무 길이가 m인 경우
        result = mid
        return
    elif total_tree > m:
        # 나무 길이가 m을 초과하는 경우
        result = mid  # 일단 현재 절단기에 설정한 높이 저장
        binary_search(mid + 1, end)  # 탐색
    else:
        # 나무길이가 m 미만인 경우
        binary_search(start, mid - 1)  # 탐색
        
# 입력 받기
n, m = map(int, sys.stdin.readline().split())
tree_ls = list(map(int, sys.stdin.readline().split()))
result = 0

# 이진 탐색을 위한 초기값 설정
start = 1
end = max(tree_ls)

binary_search(start, end)  # 이진 탐색
print(result)
