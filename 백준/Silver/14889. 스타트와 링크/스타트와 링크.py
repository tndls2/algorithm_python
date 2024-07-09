def dfs(idx, count):
    # idx: 현재 방문할 사람 인덱스
    # count: 현재까지 스타트팀에 포함된(visited=True) 사람 수
    global visited, answers, n, ability
    if count == n // 2 and idx != n:
        start_team = 0
        link_team = 0
        # 팀 나누기 끝난 경우
        for i in range(n):
            for j in range(i):
                if visited[i] and visited[j]:
                    # i와 j가 스타트 팀인 경우
                    start_team += (ability[i][j] + ability[j][i])
                elif not visited[i] and not visited[j]:
                    # i와 j가 링크 팀인 경우
                    link_team += (ability[i][j] + ability[j][i])
        # 각 팀별 능력치 합산인 끝난 경우
        # 능력치 차이 값 저장
        answers.append(abs(start_team - link_team))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True  # 스타트 팀에 포함
            dfs(i + 1, count + 1)  # 다음 사람 방문
            visited[i] = False  # 백트래킹을 위해 복구
n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n  # True인 경우: 스타트 팀/ False인 경우: 링크 팀
answers = []
dfs(0, 0)
print(min(answers))  # 능력치 차이 값 중 최솟값