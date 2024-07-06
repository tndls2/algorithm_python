### 블로그들 참고하여 해결한 문제 ###
def dfs():
    if len(sequence_list) == m:
        # 수열 길이 조건에 해당하는 경우
        print(" ".join(map(str,sequence_list)))
        return
    
    for i in range(1, n+1):
        if i not in sequence_list:
            sequence_list.append(i)
            dfs()  # for문 다중 중첩 가능
            sequence_list.pop()
        
n, m = map(int, input().split())
sequence_list = []  # 수열을 저장할 리스트
dfs()