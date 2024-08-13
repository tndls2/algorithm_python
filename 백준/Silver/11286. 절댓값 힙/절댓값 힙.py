import sys
import heapq    

n = int(input())
heap = []
for _ in range(n):
    item = int(sys.stdin.readline().rstrip())
    if item == 0:
        if len(heap) == 0:
            # 힙이 비어있는 경우
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        # item이 음수인 경우
        if item < 0:
            heapq.heappush(heap, (-item, item))  # 절댓값 기준으로 정렬되도록 함
        else:
            heapq.heappush(heap, (item, item))