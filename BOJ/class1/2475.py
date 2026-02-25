lst = list(map(int, input().split()))

total = 0
for i in range(len(lst)):
    total += lst[i] ** 2
print(total % 10)