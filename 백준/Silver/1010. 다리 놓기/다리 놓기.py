from math import comb
import sys

k = int(input())
for _ in range(k):
    n,m = map(int, sys.stdin.readline().split())
    print(comb(m,n))  # n <= m