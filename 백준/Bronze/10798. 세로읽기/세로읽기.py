words = [input() for _ in range(5)]  # 5개의 단어 입력받기
max_length = max(len(word) for word in words)  # 최대길이 체크
answer = []

for i in range(max_length):  # 최대길이만큼 탐색
    for word in words:
        if i < len(word):  # 각 단어의 길이가 다른 것 고려하기
            answer.append(word[i])
            
print(''.join(answer))  # 배열->문자열로 변환하여 출력