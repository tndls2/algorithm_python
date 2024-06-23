from collections import deque

n = int(input())
deq = deque(enumerate(map(int, input().split())))
# index도 포함하는 enumerate 이용하기
# 양방향 큐인 deque(데크)는 양끝 요소 삽입/제거 시 O(1) 소요
## cf. 리스트는 O(n) 소요됨

answer = []
for i in range(n):
    idx, removed = deq.popleft()  # popleft시 rotate(-1)도 자동으로 됨
    if removed>0:
        deq.rotate(-removed+1)  # 음수: 반시계방향 회전 ex)rotate(-1): 맨 앞에 있던게 맨 뒤로 이동
    else:
        deq.rotate(-removed)  # 양수: 시계방향 회전 ex)rotate(1): 맨 뒤에 있던게 맨 앞으로 이동
    answer.append(idx+1)  # 인덱스 저장
print(*answer)