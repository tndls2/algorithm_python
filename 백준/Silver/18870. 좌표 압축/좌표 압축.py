import sys

n = int(input())
ls = list(map(int, sys.stdin.readline().split()))
order_ls = sorted(set(ls))  # 중복 제거, 오름차순 정렬

answer = []
index_dict = {order_ls[i]: i for i in range(len(order_ls))}

for i in ls:
    answer.append(index_dict[i])
print(*answer)  # 리스트 요소 한 줄에 공백 구분하여 출력하기