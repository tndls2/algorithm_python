import sys

n = int(input())
ls = [int(sys.stdin.readline()) for _ in range(n)]
# input()이 sys.stdin.readline() 보다 느림! -> 시간초과 발생
## input(): prompt message를 출력 + 개행 문자를 삭제한 값 리턴
## sys.stdin.readline(): prompt message를 출력X + 개행 문자를 포함한 값 리턴

 
ls = sorted(ls)  # 오름차순 정렬

for i in range(len(ls)):
    print(ls[i])  # 한 줄에 하나씩 출력하기