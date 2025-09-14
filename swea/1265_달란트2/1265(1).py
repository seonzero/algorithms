from itertools import combinations_with_replacement

t = int(input())

for tc in range(1, t+1):
    #달란트개수, 묶음개수
    n, m = map(int, input().split())

    '''
    목표: m개의 곱이 최대가 되게 하기
    m개의 합은 n이다. 
    '''
    max = 0
    for comb in combinations_with_replacement(range(1, n+1), m):
        if sum(comb) == n:
            # print(comb, sum(comb))
            total = 1
            for i in comb:
                total *= i
    
            if total>max:
                max = total

    print(f'{tc} {max}')