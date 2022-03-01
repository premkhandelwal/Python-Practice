from itertools import count
from math import ceil, floor


""" 

x


"""


def isPalindrome(str1):
    if(str1[::-1] == str1):
        return 1
    return 0

n= int(input())
s = input()

m = int(input())
inputs = list(map(int,input().split()))
# pdList = []
count = 0

for i  in range(len(s) + 1):
    # print(s[i])
    for j in range(i):
        if(isPalindrome(s[j:i]) and inputs.__contains__(len(s[j:i]))):
            count += 1
print(count)            

  
""" i = 0
countPd = 0    
while(i != len(s)):
    # print(s[i:])
    # print(isPalindrome(s[i:]))
    if(isPalindrome(s[i:len(s) - i]) == 1 and len(s[i: len(s) - i])==l ):
        # and len(s[i: len(s) - i])==l
        countPd +=1

        print(s[i:len(s) - i])   
    i += 1
print(countPd) """