array = [[int(x) for x in input().split()] for _ in range(9)]
# 다른 작성법: array = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
for row in array:
    # 행 단위로 최댓값 갱신
    max_value = max(max(row), max_value)
    
index = [(i,j) for i in range(9) for j in range(9) if array[i][j] == max_value]  # 최댓값의 인덱스 찾기
print(max_value)
print(index[0][0]+1, index[0][1]+1)  # 최댓값 행 번호, 열 번호 출력 (최대값이 2개 이상인 경우 그 중 하나에 대해서만 출력)