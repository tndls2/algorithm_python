word = input()
word = word.upper()  # 모두 대문자로 변환
dict = {}  # 알파벳별 사용횟수 저장

for chr in word:
    if chr in dict:
        dict[chr] += 1  # 새로 사용함
    else:
        dict[chr] = 1  # 기존에 사용함

tmp = [k for k,v in dict.items() if max(dict.values()) == v]  # 알파벳 사용횟수의 중복 고려
if len(tmp) > 1:
    # 가장 많이 사용한 알파벳이 여러 개 존재하는 경우
    print('?')
else:
    print(tmp[0])