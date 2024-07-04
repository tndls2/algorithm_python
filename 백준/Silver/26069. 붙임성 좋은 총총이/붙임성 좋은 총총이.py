import sys
n = int(input())
dance = set()  # 무지개 댄스를 추고 있는 사람 set
for _ in range(n):
    a, b = sys.stdin.readline().split()
    if a=='ChongChong' or b=='ChongChong':
        dance.add(a)
        dance.add(b)
    elif a in dance:
        dance.add(b)
    elif b in dance:
        dance.add(a)
        
answer = len(dance)
print(answer)