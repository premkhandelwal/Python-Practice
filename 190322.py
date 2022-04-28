""" 
1,7 = 8
1,2 = 3
1,4 = 
7,2
7,4
2,4

sum = 14
orig = [1,7,2,4] = 14
k = 3 

ans = [1,7,4] = 12 - 1, 12 - 7, 12 - 4
ans11 = [1,7,2] = 10-1, 10-7, 10-2
ans1 = [8,5,11]







1,7 = 8
# 1,2 = 3
1,4 = 5
# 7,2 = 9
7,4 = 11
# 2,4 = 6

[1,2], [7,2], [2,4] = 3


sum = 14
orig = [1,7,2,4] = 14
k = 3 

ans = [1,7,4] = 12 - 1, 12 - 7, 12 - 4
ans11 = [1,7,2] = 10-1, 10-7, 10-2
ans1 = [8,5,11]

6
1
3
-5
-3
2

"""


# s = [19, 10, 12, 10, 24, 25, 22]

              
# print(ansMap)
# print(len(s)- maxCount)




s = [19, 10, 12, 10, 24, 25, 22]
# s = [1, 7, 2, 4]
k = 3
maxCount = 0
ansMap = []
ansMap1 = []
ansMap2 = []
# ansMap1= [[1,2]}

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if(((s[i] + s[j]) % k) != 0):
            ansMap.append([s[i], s[j]]) 


for i in ansMap:
    # 14 - 3, 14 - 5, 14 - 9, 14 - 11, 14 - 6
    # 11, 9, 5, 3, 8
    if(sum(s) - sum(i) % k != 0):
        print(i)
        maxCount += 1        


print(ansMap)
# print(ansMap)
print(len(s)- maxCount)