import sys

n = int(input())
ls_log = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]

dict_log = {log[0]:log[1] for log in ls_log}  # dictionary는 key가 중복 되면 마지막 값으로 value가 저장됨
ls_enter = [key for key, value in dict_log.items() if value == 'enter']

answer = sorted(ls_enter, reverse=True) # 알파벳 내림차순 정렬
print('\n'.join(answer))  # 한 줄에 하나의 요소만 출력