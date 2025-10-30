'''
모든 조합들(부분집합)을 구하고, 해당 조합들의 키의 합을 선반 높이와의 차이를 구한다. 
그리고 그 차 중 가장 작은 값을 결과로 출력한다. (set)

접근방법1. 모든 조합을 구하고, 키를 합해서, 목표 높이에 도달하는지를 본다
(from itertools import combination)
'''

from itertools import combinations

tc = int(input())

for t in range(1, tc+1):
    n, b = map(int, input().split())

    arr = list(map(int, input().split()))

    #점원들의 키의 합이 b를 넘되, 가장 작은 값을 갱신할 변수
    min_height = n * 10000 
    #min_height = float('INF') #그냥 무한을 할당함. 메모리차지하거나 그런거 아님

    #입력받은 arr에서 1명, 2명, 3명, ... , n명을 고르는 선택으로 모든 조합을 구해볼 것!
    for r in range(1, n+1):
        #r = 1,2,3
        #r=1: [1][2][3][4][5]
        #r=2: [1,2][1,3][2,3]=5...
        #r=3: [1,2,3]=6...
        comb_list = combinations(arr, r)

        #만들어진 조합들에 대해 키의 합을 구함
        #그리고 그 키의 합의 최솟값을 구한다 (조건은b보다 클 것. )
        for comb in comb_list:
            total_height = sum(comb)

            #무조건 최소값을 갱신하는 것이 아니고
            if total_height >= b:
                total_height = min(total_height, min_height)


    print(f'#{tc} {min_height-b}')

