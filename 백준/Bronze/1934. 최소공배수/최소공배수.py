def gcd(n,m):  
    # 유클리드 호제법 이용하여 최대공약수 구하기
    while m > 0:
        n, m = m, n % m
    return n
def lcm(n, m):
    # 최대공약수 이용하여 최소공배수 구하기
    return n * m // gcd(n, m)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a,b))