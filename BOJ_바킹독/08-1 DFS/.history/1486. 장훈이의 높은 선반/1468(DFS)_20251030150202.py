


tc = int(input())

for t in range(1, tc+1):
    n, b = map(int, input().split())

    arr = list(map(int, input().split()))

    min_height = float('INF')

    '''DFS에서...
    어떤 값을 파라미터로 넣을까?
    ~ DFS는 스택이 메인이다. - 끝까지 들어왔다가 다시 최근에 접근했던 함수로 돌아가는 것처럼(선입후출) - 재귀
    
    1. 재귀함수를 종료하기 위한 변수
    - 점원들을 모두 선택(포함하든/안하든)했을 때 
    - 현재 선택한 점원의 인덱스를 전달
    2. 누적해서 가져가고 싶은 값 
    - 우리가 포함한 점원들의 키의 합
    '''
    
    #idx: 현재 탐색중인 직원의 인덱스
    #h_sum: 내가 선택해온 직원들의 키의 합
    def DFS(idx, h_sum):
        global min_height

        #여태가지 선택한 직원들의 키의 합이.. 이미 우리가 선정한 최솟값보다 커졌으면
        #더이상 진행할 필요가 없다. 
        if h_sum >= min_height:
            return

        #모든 직원들에 대해서 선택이 끝났다는 의미
        if idx == n:
            if h_sum >= b:
                min_height = min(min_height, h_sum)
            return 
        
        #idx에 해당하는 직원을 선택한 경우:
        DFS(idx+1, h_sum+arr[idx])

        #idx에 해당하는 직원을 선택하지 않은 경우
        DFS(idx+1, h_sum) 

    DFS(0,0)
    print(f'#{tc} {min_height}')