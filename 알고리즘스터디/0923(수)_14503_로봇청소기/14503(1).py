# 참고: https://code-angie.tistory.com/29#google_vignette

n, m = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y): 
    return 0<=x<n and 0<=y<m

#현재 청소기의 좌표랑 방향이 주어짐
def cleaner(x, y, d):
    cnt = 0
    while True:
        # 1. 청소하기
        if area[x][y] == 0:
            area[x][y] = -1 
            cnt += 1

        
        # 2. 반시계방향으로 회전하며 (3->2, 2->1. 1->0 ,0->3)
        # 청소하지 않은 칸 탐색
        for _ in range(4):
            d = (d-1) % 4
            #각 방향들을 탐색한다
            nx = x + dx[d]
            ny = y + dy[d]

            #동서남북 중...먼지칸을 발견 - 이동 - (다시 1번으로 = 청소해라)
            if in_range(nx, ny) and area[nx][ny]==0:
                x, y = nx, ny
                break 

        else: 
            #먼지칸이 없다 -> 후진하자
            x = x + dx[d] * (-1) 
            y = y + dy[d] * (-1)

            #범위내에 있는데 벽이거나, 범위에서 벗어났다면... => 종료
            if in_range(x, y) and area[x][y] == 1 or not in_range(x, y):
                print(cnt)
                return #종료하기
            
cleaner(r,c,d)