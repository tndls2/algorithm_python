import sys

input_formula = sys.stdin.readline().rstrip()

# 가장 최솟값이 나오게 하려면 큰 값끼리 빼게 하면 됨
# + 먼저 계산 -> - 이후 계산
num_ls = []
first_group_formula = input_formula.split('-')  # -로 먼저 구획 나누기
for group_formula in first_group_formula:
    second_group_formula = group_formula.split('+') # +로 이후 구획 나누기
    total = 0
    for i in second_group_formula:
        total += int(i)  # 더하기 연산
    num_ls.append(total)  # 빼기 연산할 리스트에 저장

answer = num_ls[0]
for i in range(1, len(num_ls)):
    answer -= num_ls[i]
print(answer)