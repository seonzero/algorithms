'''
행렬... 진짜 모르겠다!!

찾아낸 행렬의 개수와 행렬의 정보 출력! (1*2, 4*3 이런거)
'''
import heapq

def find_row_col(arr, row, col):
    c_count = 1 #(1,1에서 시작했다고 가정하고 얼마나 이동하는지 세보는거임)
    r_count = 1

    next_row = row
    #다음행(아래)에도 물건이 있는지 보기 
    while arr[next_row][col] !=0:
        next_col = col

        #다음행-의 좌표에도 있는지 보기
        while arr[next_row][next_col] !=0:
            if next_row == row:
                c_count += 1
            #왜 0으로 만들지...? 
            arr[next_row][next_col] = 0
            #다음 열로 넘어가기
            next_col += 1
            if not (0 <= next_col < n): break
        
        #다음 행으로 넘어가기
        r_count += 1
        next_row += 1
        if not (0 <= next_row < n): break        

    #마지막 칸의 이동횟수를 전달해주는거같음 (2,3 이런거)
    return r_count -1, c_count-1, (r_count-1)*(c_count-1)


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    #n*n행렬
    arr = [ list(map(int, input().split())) for _ in range(n)]

    result = []
    count = 0 

    #행렬을 돌아봅시다 - 각 행마다 / 각 열을 돌아본다
    for row in range(n):
        for col in range(n):
            #0보다 크다: 물건이 있다
            if [row][col] > 0:
                #배열의 정보와 row, col좌표를 넘겨준다.
                # (r_)의 뜻은?? 
                r_row, r_col, r_sum = find_row_col(arr, row, col)
                heapq.heappush(result, (r_sum, r_row, r_col))
                count +=1

    print(f'#{tc} {count}', end=' ')
    for _ in range(count):
        a,b,c = heapq.heappop(result)
        print(f'{b} {c}', end= ' ')
    print()