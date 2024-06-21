import queue

n, k = map(int, input().split())
josephus_queue = queue.Queue()

# 원소 삽입
for i in range(1, n + 1):
    josephus_queue.put(i)

# 원소 제거
answer = []
for _ in range(n):
    for _ in range(k - 1):
        n = josephus_queue.get()
        josephus_queue.put(n)
    removed = josephus_queue.get()
    answer.append(removed)

print('<', end='')
print(', '.join(map(str, answer)), end='')
print('>')