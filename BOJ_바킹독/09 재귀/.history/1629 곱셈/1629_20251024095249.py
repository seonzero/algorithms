a,b,c = map(int, input().split())

def func(a,b,cnt, result):
    if cnt == b:
        return result
    result = result * a
    func(a,b,cnt+1, result)

result = func(a,b, 0, 1)

print(result)