"""
1-10   2,3,5,7
11-20  11,13.17, 19
21-30  23,29
31-40  31,37
2,3,5,7
2,3,5,7,11
2,3,5,7,11,13

50


"""
def isPrime(num):
    if(num < 1):
        return 1
    if(num == 1):
        return 0    
    i = 2    
    while(i <= num/2):
        if(num % i == 0):
            return 0
        i+=1    
    return 1        


def countPrime(num):
    count = 0
    arrPrime = []
    for i in range(1,num+1):
        if(isPrime(i)):
            arrPrime.append(i)
    return arrPrime

num = int(input())
traverseCount = 0
arr = countPrime(num)
print(arr)
currCount = num
print(len(arr))
# print(len(arr) < 2)
while(len(arr) > 3):
    print("len", len(arr))
    traverseCount += 1
    currCount -= len(arr)
    val = 0
    for i in arr:
        if(i < currCount):
            arr = arr[:i] 
            break
       
    print(
        "arr",arr)
    print(val)   
    

print(traverseCount + 1)    
