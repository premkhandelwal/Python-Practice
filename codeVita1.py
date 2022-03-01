def isPalindrome(str1):
    if(str1[::-1] == str1):
        return 1
    return 0

n= int(input())
s = input()

m = int(input())
inputs = list(map(int,input().split()))
count = 0

for i  in range(len(s) + 1):
    for j in range(i):
        if(isPalindrome(s[j:i]) and inputs.__contains__(len(s[j:i]))):
            count += 1           
print(count, end="")      