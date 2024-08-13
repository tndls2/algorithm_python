## 다른 사람 풀이 참고함 : 인덱스를 활용하는 아이디어 
import sys

n = int(input())
array = list(map(int, sys.stdin.readline().split()))

answer = [-1] * n  # 오최값 못 찾으면 -1 반환
stack = [0]  # 0번 인덱스 일단 넣음
for i in range(1, n):
    while stack and array[stack[-1]] < array[i]: # 스택이 채워져 있고, 스택의 마지막 요소보다 값이 큰 경우
        answer[stack.pop()] = array[i]  # 스택의 마지막 요소 오최값
    stack.append(i)  # 스택에 값 넣기
    
print(' '.join(map(str, answer)))