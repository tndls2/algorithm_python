import sys
n = int(sys.stdin.readline().rstrip())
meeting_ls = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
meeting_ls.sort(key = lambda x: (x[1], x[0]))  # 회의 종료 시각 기준 오름차순 정렬
# 접근 유형
# 1. 시작 시각 기준 오름차순 정렬 : 회의 시간은 반영하기 어려움
# 2. 회의 시간 짧은 기준 오름차순 정렬 : 회의의 시작 시각/종료시간 반영하기 어려움
# 3. 종료 시간 기준 오름차순 정렬 : 끝나는 시각이 빠르다는 것은 시작 시각이 빠름 + 회의 시간이 짧은 것을 동시에 포함함 <-choose
answer = 0
ending_time = 0
for i in range(n):
    if meeting_ls[i][0] >= ending_time:  
        # 현재 회의 시작 시각이 이전 회의 종료 시각보다 크거나 같은 경우
        ending_time = meeting_ls[i][1]
        answer += 1
print(answer)