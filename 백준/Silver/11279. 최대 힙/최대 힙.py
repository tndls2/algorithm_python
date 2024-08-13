import sys
import heapq

n = int(input())

max_heap = []  # 최대힙
for _ in range(n):
    item = int(sys.stdin.readline().rstrip())
    if item == 0:
        if len(max_heap) == 0:
            # max_heap이 빈 배열이 경우
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap,(-item, item))  # y = -x 변환 -> 최솟값 정렬이 최댓값 정렬로 바뀜