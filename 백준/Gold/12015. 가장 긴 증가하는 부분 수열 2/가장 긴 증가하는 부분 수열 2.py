## 최장 증가 부분 수열(LIS, Longest Increasing Subsequence) 문제 
## 방법론 참조 -> https://www.youtube.com/watch?v=voklbG1wU8A
import sys
def binary_search(target, start, end):
    global lis_ls
    
    while start < end:
        mid = (start + end) // 2
        if lis_ls[mid] < target:
            # 중간값 초과인 경우 
            start = mid + 1  # 다음 탐색이 중간값보다 큰 쪽
        else: 
            # 중간값 이하인 경우
            end = mid
    return end
n = int(sys.stdin.readline().rstrip())
sequence_ls = list(map(int, sys.stdin.readline().split()))  # 수열 A
lis_ls = [sequence_ls[0]]
for element in sequence_ls:
    if element > lis_ls[-1]:
        # 마지막 원소 초과 값인 경우 -> 추가
        lis_ls.append(element)  # 항상 오름차순 정렬되어 있음
    else:
        # 마지막 원소 이하 값인 경우 -> 교체 by.lower bound 방식
        i = binary_search(element, 0, len(lis_ls))  # 교체할 자리 찾기 - O(nlogn)
        lis_ls[i] = element
result = len(lis_ls)
print(result)