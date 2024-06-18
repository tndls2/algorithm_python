n = int(input())
for i in range(1, n+1):
    digit_sum = i + sum(map(int, str(i)))  # map은 이터레이터 반환 ex. 216 -> (2,1,6)
    if digit_sum == n:
        print(i)
        break
    if i==n:  # 생성자가 없는 경우
        print(0)
