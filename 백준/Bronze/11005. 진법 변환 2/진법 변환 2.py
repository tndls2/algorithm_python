num_36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int, input().split())
answer = ''

while(n!=0):
    answer+=num_36[n % b]  # 나머지 값 b진법으로 변환
    n = n // b  # 정수 몫

print(answer[::-1])  # 문자열 뒤집기