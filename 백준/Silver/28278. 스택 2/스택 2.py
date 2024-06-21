import sys
n = int(input())
stack = []
for _ in range(n):
    inputs = list(map(int, sys.stdin.readline().split()))
    # 명령어와 그에 따른 값을 분리
    cmd = inputs[0]    
    match cmd:
        case 1:  
            # i를 스택에 넣음
            i = inputs[1]
            stack.append(i)
        case 2:
            # 스택에 정수가 있으면 맨 위의 정수를 제외하고 출력
            if len(stack)==0: # 예외
                print(-1)
            else:
                print(stack.pop())
        case 3:
            # 스택에 있는 정수 개수 출력
            print(len(stack))
        case 4:
            # 스택이 비었으면 1, 아니면 0 출력
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        case 5:
            # 스택에 정수가 있으면 맨 위의 정수 출력
            if len(stack) == 0:  # 예외
                print(-1)
            else:
                print(stack[-1])