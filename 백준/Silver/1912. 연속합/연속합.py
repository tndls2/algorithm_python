import sys

n = int(sys.stdin.readline().rstrip())
sequence_ls = list(map(int, sys.stdin.readline().split()))

for i in range(len(sequence_ls)-1):
    # 이전 원소들과의 최대 합 vs 현재 원소값 중 최댓값으로 update
    sequence_ls[i+1] = max(sequence_ls[i]+sequence_ls[i+1], sequence_ls[i+1])
    
print(max(sequence_ls))
