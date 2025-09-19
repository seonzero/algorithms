n = input()
set = [0] * 10

for i in n:
    num = int(i)

    if num == 6 or num ==9:
        if set[6]<set[9]:
            set[6] += 1
        else:
            set[9]+=1

    else:
        set[num] +=1


print(max(set))