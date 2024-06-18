n = int(input())
if n<3:
    # 예외
    print(-1)
    
elif n%5==0:
    # 5로 나누어 떨어지는 경우
    answer = n//5
    print(answer)
else:   
    for i in range(n//5, -1, -1):  # 역순(최대한 5kg 봉지 사용 -> 갯수 최소화)
        if i==0:
        # 5kg 봉지를 사용할 수 없는 경우
            if n%3 == 0:
                # 3으로 나누어 떨어지는 경우
                answer = n // 3
                print(answer)
                break
            else:
                # 예외
                print(-1)
                break
            
        new_n = n - 5 * i
        if new_n%3==0:
            # 3으로 나누어 떨어지는 경우
            answer = i + new_n//3
            print(answer)
            break