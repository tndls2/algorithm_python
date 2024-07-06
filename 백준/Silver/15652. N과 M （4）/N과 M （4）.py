def dfs():
    if len(sequence_list) == m:
        # 수열 길이 조건에 해당하는 경우
        print(" ".join(map(str,sequence_list)))
        return
    
    for i in range(1, n+1):
        # 중복 허용
        if not sequence_list or sequence_list[-1] <= i:
            # 비내림차순
            sequence_list.append(i)
            dfs()
            sequence_list.pop()
        
n, m = map(int, input().split())
sequence_list = []  # 수열을 저장할 리스트
dfs()