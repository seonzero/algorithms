s1 = input()
s2 = input()

arr1 = [0] * 26
arr2 = [0] * 26

#1000번
for i in s1:
    arr1[ord(i)-97] +=1

#1000번
for i in s2:
    arr2[ord(i)-97] +=1

count = 0
for i in range(26):
    if arr1[i] != arr2[i]:
        count += abs(arr1[i] - arr2[i])
    
print(count)