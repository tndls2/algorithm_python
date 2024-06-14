n=1000  # n은 1,000 이하의 자연수

''' 에라토스테네스의 체 이용하여 소수 구하기 '''
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

''' 입력 받기 '''
cnt = int(input())
numbers = list(map(int, input().split()))

''' 소수인지 판별 '''
answer = 0
for number in numbers:
    if number in primes:
        answer += 1
print(answer)