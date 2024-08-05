import sys
import itertools

n, k = map(int, sys.stdin.readline().split())
# 2 <= n <= 100,000
temperature_ls = list(map(int, sys.stdin.readline().split()))
accumulate_ls = [0] + list(itertools.accumulate(temperature_ls))  # temperature_ls에 대한 부분 누적합 저장
k_day_sum_ls = []

sum = 0
for i in range(k, n+1):
    k_day_sum_ls.append(accumulate_ls[i] - accumulate_ls[i-k])
print(max(k_day_sum_ls))