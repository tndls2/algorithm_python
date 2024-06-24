import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
answer = deque()

for i in range(n):
    if a[i]==0:  # i번째 자료 구조:큐(선입선출)
        # 스택(후입선출)인 경우 -> 기존 원소값 필요없음
        answer.appendleft(b[i])
for j in range(m):
    answer.append(c[j])
       
for _ in range(m):
    # 삽입한 수열의 길이만큼 출력됨
    # 기존 원소가 우선 출력된 후, 삽입한 원소가 출력됨
    print(answer.popleft(), end=" ")
