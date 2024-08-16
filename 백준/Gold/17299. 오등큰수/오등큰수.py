import sys
from collections import Counter
n = int(input())
array = list(map(int, sys.stdin.readline().split()))

count_dict = Counter(array)  # Counter 사용하여 각 원소별 빈도수 저장

answer = [-1] * n
index_stack = [0]  # 0번 인덱스 일단 넣음

for i in range(1, n):
    while index_stack and count_dict[array[index_stack[-1]]] < count_dict[array[i]]:
        # 스택이 채워져 있고, 스택의 마지막 원소의 빈도수보다 새로 입력하는 원소의 빈도수가 큰 경우
        answer[index_stack.pop()] = array[i]
    index_stack.append(i)

print(' '.join(map(str, answer)))    