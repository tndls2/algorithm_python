n = int(input())

cnt = 1  # 지나가는 방의 수
max_num = 1  # 같은 레이어에서 최댓값

while max_num < n:
    max_num += 6*cnt
    cnt+=1
print(cnt)