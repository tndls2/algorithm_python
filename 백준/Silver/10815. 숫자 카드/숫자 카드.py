import sys

n = int(input())
card_ls = list(map(int, sys.stdin.readline().split()))
card_dict = {card_ls[i]: 1 for i in range(len(card_ls))}  # 상근이가 가지고 있으면 1

m = int(input())
check_ls = list(map(int, sys.stdin.readline().split()))
answer = []
for check in check_ls:
    
    if check in card_dict:
        # 상근이가 가지고 있으면 1
        answer.append(card_dict[check])
    else:
        # 상근이가 가지고 있지 않으면 0
        answer.append(0)
print(*answer)