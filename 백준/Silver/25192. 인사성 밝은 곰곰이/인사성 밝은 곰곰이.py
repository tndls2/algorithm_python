import sys
n = int(input())
greeting = {}
answer = 0
count = 0
for i in range(n):
    chatting = sys.stdin.readline().rstrip()
    if chatting == 'ENTER':  # 새로운 사람이 입장한 경우
        answer += count
        count = 0  # 기존 데이터 초기화
        greeting = {}  # 기존 데이터 초기화
    else:  # 채팅을 하는 경우
        if chatting in greeting:
            continue  # 이미 인사한 내역이 있으면 pass
        greeting[chatting] = 1  # 처음 채팅
        count += 1
if count!=0:  # for문 종료 후 데이터 저장
    answer += count
print(answer)