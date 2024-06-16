import itertools

n, m = map(int,input().split())
ls = sorted(list(map(int, input().split())))

ls_sum = []
answer = 0

for combination in itertools.combinations(ls,3):  # 조합 이용
	ls_sum.append(sum(list(combination)))  # combinations 결과인 튜플 -> 리스트로 변환
ls_sum = sorted(ls_sum)  # 오름차순 정렬

for element in ls_sum:
    if answer < element and element <= m:
        answer = element
    if element >= m:
        break
print(answer)