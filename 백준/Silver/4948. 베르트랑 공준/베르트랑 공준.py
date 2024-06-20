n=123456  # n은 123,456 이하의 정수
''' 에라토스테네스의 체 이용하여 소수 구하기 '''
a = [False,False] + [True]*(2*n-1)
ls_primes=[]  # 소수 리스트
for i in range(2,2*n+1):
  if a[i]:
    for j in range(2*i, 2*n+1, i):
        a[j] = False

while 1:
    n = int(input())
    if n==0:  # 입력의 마지막=0
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        # n~2*n 범위 안에 있는 소수 세기
        if a[i]==True:
            cnt +=1
    print(cnt)