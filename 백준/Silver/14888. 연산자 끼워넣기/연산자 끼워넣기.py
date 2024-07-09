def dfs(count, current_result):
    if count == n:
        results.append(current_result)
        return
    
    for operator in operators:
        if operator_dict[operator] > 0:
            operator_dict[operator] -= 1
            next_result = current_result
            
            if operator == '+':
                next_result += operand_ls[count]
            elif operator == '-':
                next_result -= operand_ls[count]
            elif operator == '*':
                next_result *= operand_ls[count]
            elif operator == '//':
                if next_result < 0 and operand_ls[count] > 0:
                    next_result = -(-next_result // operand_ls[count])
                else:
                    next_result //= operand_ls[count]
            
            dfs(count + 1, next_result) # 다음 피연산자에 대해 순회
            operator_dict[operator] += 1  # 백트래킹을 위해 연산자 개수를 복구

n = int(input())
operand_ls = list(map(int, input().split()))  # 피연산자

operators = ['+', '-', '*', '//']  # 이때 나눗셈은 정수 나눗셈으로 몫만 취함
operator_count = list(map(int, input().split()))
operator_dict = dict(zip(operators, operator_count))  # 연산자별 갯수를 저장한 딕셔너리

results = []
dfs(1, operand_ls[0])

print(max(results))  # 최댓값
print(min(results))  # 최솟값
