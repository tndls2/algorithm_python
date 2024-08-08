import sys
import itertools
    
n = int(input())
line_ls = list(map(int, sys.stdin.readline().split()))
line_ls.sort()
sum_ls = list(itertools.accumulate(line_ls))
print(sum(sum_ls))