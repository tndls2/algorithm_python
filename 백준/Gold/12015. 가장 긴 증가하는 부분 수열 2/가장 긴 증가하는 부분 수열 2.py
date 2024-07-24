## 최장 증가 부분 수열(LIS, Longest Increasing Subsequence) 문제 
## lower bound = 배열에서 특정 값 '이상'이 처음으로 나타나는 위치 찾기
## upper bound = 배열에서 특정 값을 '초과'하는 값이 처음으로 나타나는 위치 찾기
## 방법론 참조 -> https://www.youtube.com/watch?v=voklbG1wU8A

import sys

def binary_search(target, start, end):
    global lis_ls
    
    while start < end:
        mid = (start + end) // 2
        if lis_ls[mid] < target:
            # target이 중간 값 초과인 경우 
            start = mid + 1  # 다음 탐색이 중간값보다 큰 쪽
        else: 
            # target이 중간값 이하인 경우
            end = mid  # 일단 mid 저장 ( = 처음으로 target 이상의 값이 나타난 위치 저장 = lower boundary)
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
