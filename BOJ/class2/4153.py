while 1:
    a, b, c = map(int, input().split())
    
    if a==0: 
        break
    
    #가장 큰 변 찾기 ~ 만약 같은 길이가 2개라면?
    max_num = max(a,b,c)

    if a==b or b==c or c==a or (a==b and b==c):
        print("wrong")
        continue

    if max_num == a:
        num1, num2 = b, c
    elif max_num==b:
        num1, num2 = c,a
    else:
        num1, num2 = a,b

    #피타고라스 정리 적용
    if max_num ** 2 == num1**2 + num2**2:
        print("right")
    else:
        print("wrong")