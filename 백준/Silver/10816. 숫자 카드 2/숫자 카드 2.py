import sys

n = int(input())
card_ls = list(map(int, sys.stdin.readline().split()))

card_dict = {}
for card in card_ls:
    if card in card_dict:  # 이미 나온 숫자
        card_dict[card] += 1
    else:  # 처음 나온 숫자
        card_dict[card] = 1
        
m = int(input())
check_ls = list(map(int, sys.stdin.readline().split()))
answer = []
for check in check_ls:
    if check in card_dict:  # dict에 있는 숫자
        answer.append(card_dict[check])
    else:  # dict에 없는 숫자
        answer.append(0)
print(*answer)