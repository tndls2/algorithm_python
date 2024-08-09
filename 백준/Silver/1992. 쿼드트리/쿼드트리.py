## 쿼드트리 문제
## 쿼드트리(Quad Tree) : 자식 노드가 4개인 트리

def compress_video(x, y, size):
    global answer
    
    color = video_ls[x][y]  # 현재 사각형의 첫 번째 색상
    
    if size == 1:  # 더 이상 쪼갤 수 없는 최소 크기인 경우
        answer.append(color)
        return
    
    # 현재 사각형의 모든 픽셀이 동일한 색상인지 확인
    is_same_color = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if video_ls[i][j] != color:
                is_same_color = False
                break
        if not is_same_color:
            break

    if is_same_color:
        answer.append(color)
    else:
        # 4개의 사분면으로 분할
        half_size = size // 2
        answer.append("(")
        compress_video(x, y, half_size)  # 왼쪽 위
        compress_video(x, y + half_size, half_size)  # 오른쪽 위
        compress_video(x + half_size, y, half_size)  # 왼쪽 아래
        compress_video(x + half_size, y + half_size, half_size)  # 오른쪽 아래
        answer.append(")")

n = int(input())
video_ls = [list(input().strip()) for _ in range(n)]
answer = []

# 비디오 압축
compress_video(0, 0, n)
print(''.join(answer))  # 리스트의 요소들을 한 번에 문자열로 출력
