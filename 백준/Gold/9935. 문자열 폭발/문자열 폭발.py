import sys

string = sys.stdin.readline().rstrip()
pop_string = sys.stdin.readline().rstrip()  # 폭발 문자열
stack = []  # 리스트로 stack 구현
pop_string_len = len(pop_string)

for letter in string:
    stack.append(letter)  # 스택에 글자를 넣음
    
    # 스택의 끝에서 폭발 문자열 길이만큼을 비교
    if ''.join(stack[-pop_string_len:]) == pop_string:
        # 폭발 문자열과 일치하면 제거
        del stack[-pop_string_len:]

# 결과 출력
answer = ''.join(stack)
if answer:
    print(answer)
else:
    print('FRULA')
