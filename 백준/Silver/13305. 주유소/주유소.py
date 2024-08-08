import sys

n = int(input())
road_ls = list(map(int, sys.stdin.readline().split()))
country_ls = list(map(int, sys.stdin.readline().split()))

min_price = country_ls[0]  # 첫 번째 주유소 가격이 일단 최솟값
total_cost = 0
for i in range(n-1):
    if country_ls[i] < min_price:
        # 주유소를 방문하면서 이전 주요소보다 현재 주유소의 가격이 저렴한 경우
        min_price = country_ls[i]
    total_cost += min_price * road_ls[i]  # 현재 주유소 ~ 더 저렴한 주유소까지의 거리까지 갈 만큼먼 현재 주요소에서 기름 충전함
print(total_cost)