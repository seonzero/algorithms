# 두 개가 똑같은 알파벳을 가지고 있는지 비교해야함. 
# newt twan - 불가능 e랑 a뭐임?
# 각각의 문자열의 길이는 최대 1000

#개수가 같은지 비교.? 아까전에 각각 알파벳 개수를 보면 되려나?????????
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s1, s2 = map(str, input().split())

    alpha1 = [0] * 26
    alpha2 = [0] * 26
    # print(f'alpha1: {alpha1}')
    # print(f'alpha2: {alpha2}')

    for i in s1:
        idx = ord(i)-97
        # print(idx, end=" ")
        alpha1[idx] += 1
    # print(f'after alpha1: {alpha1}')

    for i in s2:
        idx = ord(i)-97
        # print(idx, end=" ")
        alpha2[idx] += 1
    # print(f'after alpha1: {alpha1}')


    if alpha1 == alpha2:
        print('Possible')
    else: 
        print('Impossible')