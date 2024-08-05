import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
# 1 ≤ N ≤ 100,000 
# 1 ≤ M ≤ 100,000
# input() 사용시 시간 초과 발생

n_ls = list(map(int, sys.stdin.readline().split()))
accumulate_ls = [0] + list(itertools.accumulate(n_ls))  # n_ls에 대한 부분 누적합 저장
## 부분 누적합 -> itertools.accumulate 활용
## accumulate([1,2,3,4,5]) → 1 3 6 10 15
## accumulate([1,2,3,4,5], initial=100) → 100 101 103 106 110 115
## accumulate([1,2,3,4,5], operator.mul) → 1 2 6 24 120
        
for _ in range(m):
    start_index, end_index = map(int, sys.stdin.readline().split())
    answer = accumulate_ls[end_index] - accumulate_ls[start_index-1]
    print(answer)
