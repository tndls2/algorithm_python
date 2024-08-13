import sys
def divide_and_conquer(x, y, size):
    global answer
    num = paper_ls[x][y]  # 종이의 첫번째 번호
    # 종이 크기가 1인 경우
    if size == 1:
        answer[num] += 1
        return
    # 현재 종이가 모두 같은 수로 되어 있는지 확인
    is_same_num = True
    for i in range(size):
        for j in range(size):
            if paper_ls[x + i][y + j] != num:
                is_same_num = False  # 다른 번호를 가짐
                break
    if is_same_num:
        # 종이 내 모든 번호가 동일한 경우
        answer[num] += 1
    else:
        # 종이 내 다른 번호가 있는 경우 -> 9분할해서 탐색
        thirds_size = size // 3  # size = 3^k
        for i in range(3):
            for j in range(3):
                divide_and_conquer(x + i * thirds_size, y + j * thirds_size, thirds_size)
                
n = int(input())
paper_ls = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]
answer = {-1: 0, 0: 0, 1: 0}  # -1, 0, 1 종이 갯수 초기 상태=0
divide_and_conquer(0, 0, n)

for key, value in enumerate(answer):
    print(answer[value]) 