import math
import sys

def cantor_set(start, length, blank_set):
    if length == 1:
        return
    
    split_length = length // 3  # 3등분
    mid_start = start + split_length
    mid_end = start + 2 * split_length
    
    blank_set.update(range(mid_start, mid_end))  # 중간 문자열은 공백이 됨
    
    cantor_set(start, split_length, blank_set)  # 첫번째 문자열에 대해 재귀
    cantor_set(mid_end, split_length, blank_set)  # 마지막 문자열에 대해 재귀

while True:
    try:
        n = int(input().strip())
        length = int(math.pow(3, n))  # 3^n개의 -로 이뤄진 문자열
        line = '-' * length  # 초기 문자열
        blank_set = set()  # 공백이 될 문자열 요소
        cantor_set(0, length, blank_set)
        
        # 결과 출력
        for i in range(length):
            if i in blank_set:
                print(" ", end="")
            else:
                print("-", end="")
        print()  # 줄바꿈
    except EOFError:
        # 더 이상 입력이 없으면 종료
        break
