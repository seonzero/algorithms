#재귀와 관련된 부분을 집중해서 보자
#폭탄을 놓아야 하는 부분 

n = int(input())
grid = [ list(map(int, input().split())) for _ in range(n) ]

bombs = []
for y in range(0,n):
    for x in range(0,n):
        if grid[y][x] != 0:
            bombs.append( (y, x))


def count_area():
    


#폭탄을 한 곳에 놓는다
def KFC():
    if len(bombs)==0:
        ans = max(ans, count_area())
        return 
    
    # 폭탄을 꺼낸다
    (y, x) = bombs.pop()
    
    for i in range(0,3):
        grid[y][x] = i

    bombs.append( (y, x) )


KFC()