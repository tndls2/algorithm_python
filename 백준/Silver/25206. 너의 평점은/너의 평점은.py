score_dict = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}  # 학점 계산
credit_sum = 0
score_tmp = 0

for _ in range(20):
    subject, credit, score= input().split()
    credit = float(credit)
    
    if score == 'P':  # P는 계산 제외(예외사항)
        continue
    
    int_score = score_dict.get(score[0])  # 학점을 숫자로 변환
    if len(score)>1 and score[1]=='+':
        int_score += 0.5  # 학점 변환
    score_tmp += credit*int_score
    credit_sum += credit

total_score = score_tmp/credit_sum
print(total_score)