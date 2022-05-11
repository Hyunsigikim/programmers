def solution(A, B):
    A.sort() # 작은 순으로 정렬(시간짧음)
    B.sort()

    a = 0;#A의 인덱스 위치 잡기
    b = 0;#B의 인덱스 위치 잡기
    answer = 0;

    while(True): # 반복

        if A[a] < B[b]:# 현재의 a보다 b가 큰경우
            a+=1
            b+=1
            answer+=1 # 승리 1회 올리고 다음으로 진행
        else : # a보다 b가 작은 경우
            b+=1 # 다음 b로 이동 정렬로 인하여 뒤로갈수록 값이 커짐 
        if b==len(B):
            break# b가 끝났을 경우 반복종료

    return answer # 정답출력

A,B = [5,1,3,7],[2,2,6,8]
result=3
print(solution(A,B))