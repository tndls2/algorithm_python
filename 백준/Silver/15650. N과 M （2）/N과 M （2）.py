def dfs(start):
    if len(sequence_list) == m:
        # 수열 길이 조건에 해당하는 경우
        print(" ".join(map(str,sequence_list)))
        return
    
    for i in range(start, n+1):
        if i not in sequence_list:
            sequence_list.append(i)
            dfs(i+1)  # i보다 큰 수에 대해서만 탐색 가능
            sequence_list.pop()
        
n, m = map(int, input().split())
sequence_list = []  # 수열을 저장할 리스트
dfs(1)