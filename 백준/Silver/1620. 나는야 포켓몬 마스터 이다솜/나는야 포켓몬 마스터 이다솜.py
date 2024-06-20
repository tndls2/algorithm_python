import sys
n, m = map(int, input().split())

ls_pokemon = [sys.stdin.readline().rstrip() for _ in range(n)]  # rstrip()으로 개행문자 제거
# dict 2개로 분리
dict_name = {i+1: pokemon for i, pokemon in enumerate(ls_pokemon)}  # 포켓몬 이름 조회
dict_index = { pokemon: i+1 for i, pokemon in enumerate(ls_pokemon)}  # 포켓몬 번호 조회

answer = []
ls_test = [sys.stdin.readline().rstrip() for _ in range(m)]
for test in ls_test:
    if test.isdigit():  # 숫자 입력된 경우
        answer.append(dict_name[int(test)])  # 해당 번호의 포켓몬 이름 출력(str->int)
    else:  # 단어 입력된 경우
        answer.append(str(dict_index[test]))  # 해당 이름의 포켓몬 번호 출력(int->str)
print('\n'.join(answer))