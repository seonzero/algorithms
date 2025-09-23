n = int(input())
number = []
ans = 0

# 각 자리마다 선택할 수 있는 숫자: 4개
# n자리를 골라야 한다
# 4^n의 시간복잡도를 가진다 = 4^10 = 2^20 = 백만 ... 되게 빠른 해결 가능

#고른 숫자를 하나씩 넣어주자
def is_beautiful():
    
    #number배열을 살펴보며
    #이배열이아름다운수인지를판단해서
    #t/f를 리턴해주면 된다. 
    curr_idx = 0

    for i in range(1, n+1):
        if number[curr_idx] == number[i]:
            continue
        else: 
            #몇개가 연속되는지 파악하자
            cnt = i - curr_idx
            if cnt & number[curr_idx] % cnt !=0:
                #아름다운 수가 될 수 없다
                return False
            curr_idx = i

    #cnt: 인덱스의 차
    cnt = n - curr_idx +1

    if cnt % number[curr_idx] != 0:
        return False

    pass


def pick(cnt):
    global ans

    #종료조건
    if cnt == n:
        if is_beautiful():
            ans += 1
        return

    #다음숫자 cnt+1번째 숫자를 골라야 한다. 
    for i in range(1, 5):
        number.append(i)
        pick(cnt+1)
        number.pop() #백트래킹

pick(0) #cnt는 현재 몇번째 자리까지 골랐는지를 나타냄

'''강사님 코드
n = int(input())
number = []
ans = 0

def is_beautiful():
    curr_idx = 0
    for i in range(1, n):
        if number[curr_idx] == number[i]:
            continue
        else:
            cnt = i - curr_idx
            if cnt % number[curr_idx] != 0:
                return False
            curr_idx = i

    cnt = n - curr_idx

    if cnt % number[curr_idx] != 0:
        return False

    return True

def pick(cnt):
    global ans

    # 종료조건
    if cnt == n:
        if is_beautiful():
            ans += 1
        return

    # cnt + 1번째 숫자를 골라야 한다.
    for i in range(1, 5):
        number.append(i)
        pick(cnt + 1)
        number.pop() # 백트래킹


pick(0) # cnt: 현재 몇 번째 자리까지 골랐는지.
print(ans)

'''