from collections import Counter
import sys

n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline().rstrip()))

num_list = sorted(num_list)  # 오름차순 정렬

# 산술평균
average = int(round(sum(num_list)/n, 0) ) # 소수점 이하 첫째 자리에서 반올림
print(average)

# 중앙값
mid = n // 2  # n은 항상 홀수, 리스트 인덱스 0부터 시작
print(num_list[mid])

# 최빈값
counter = Counter(num_list)
commons = counter.most_common(2)
if len(commons) > 1 and commons[0][1] == commons[1][1]:  # 최빈값이 여러 개일 때 -> 두번째로 작은 값 출력
    print(commons[1][0])
else:
    print(commons[0][0])  # 유일한 최빈값인 경우
    
# 범위
range_value = num_list[-1] - num_list[0]  # 최소값~최대값
print(range_value)