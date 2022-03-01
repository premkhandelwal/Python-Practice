""" 
0 1 2 3 4 5 6 7 8 9 
A B C D E F G H I J

0 1 2 3 4 5 6 7 8 9 
A E I B D F H J C G

Key length = 3

A _ _ _ E _ _ _ I _ = 4

a B _ D e F _ H i J = 1


    0   1   2   3   4   5   6   7   8   9

0   A               E               I
1       B       D       F       H       J
2           C               G
                 
0 1 2 3 4 5 6 7 8 9 
A E I B D F H J C G


    0   1   2   3   4   5   6   7   8   9

0   A               D               C 
1       E       B       F       J        G
2           I               H


    0   1   2   3   4   5   6   7   8   9

0   A   _   _   _   _   _   G   _   _   _   = 5 
1   _   B   _   _   _   F   _   H   _   _   = 1
2   _   _   C   _   E   _   _   _   I   _   = 3
3   _   _   _   D   _   _   G   _   _   J   = 2



0   A   _   _   _   _   _   _   _   I   _           = 3 
1   _   B   _   _   _   _   _   H   _   J           = 1
2   _   _   C   _   _   _   G   _   _   _  K        = 3
3   _   _   _   D   _   F   _   _   _   _  _  L         = 2
3   _   _   _   _   E   _   _   _   _   _  _  _  M       = 8

key = 3 


0 1 2
3 1 2


    0   1   2   

0   A                             
1       B                  
2           C               
3       D
4   E    
5       F
6           G
7       H
8   I
9       J

col += (row%key or key) 
print(0%3 or 3)



---------------------------------------------------------------------------------------


col,row = 0
col += (row%3 or 3) =0+ 3(+1) =4

col = 4, row = 0
col += (0% 3 or 3) =4 + 3 (+ 1) = 8

col = 8, row = 0
col += (0 % 3 or 3) = 8 + 3 (+1) = 12


---------------------------------------------------------------------------------------

col = 0, row = 1
col += (1%3 or 3) = 0 + 1 + 1  = 2


col = 1, row = 1
col += (1% 3 or 3) = 1 + 1 +1 = 3

col = 3, row = 1
col += (1%3 or 3) = 3 + 1 + 1 = 5

col = 5, row = 1
col += (1%3 or 3) = 5 + 1 + 1 = 7

col = 7, row = 1
col += (1%3 or 3) = 7 + 1 + 1 = 9

---------------------------------------------------------------------------------------


col = 0, row = 2
col += (2%3 or 3) = 0 + 2 + 1 = 3

col = 3, row = 2
col += (2%3 or 3) = 3 + 2 + 1 = 5 






"""

""" 
k  = 0
for l -> row = key - 1 -> k = -1
row = row - 1

for l -> row = row - 1
"""

def encryption(message, key):
    arr = [["" for _ in range(len(message))]  for _ in range(key)] 
    row = 0 
    col = 0
    k = -1
    for i in range(len(message)):
        arr[row][col] = message[i]
        col+=1
        if(row == key - 1 or row == 0):
            k = k*(-1)
        row += k

    for i in range(key):
        for j in range(len(message)):
            if(arr[i][j] != ""):
                print(arr[i][j] , end="") 

    print("")



def decryption(message, key):
    arr = [["" for _ in range(len(message))]  for _ in range(key)]
    row = 0
    col = 0
    k = -1 
    for i in range(len(message)):
        arr[row][col] = "*"
        col += 1
        if(row == key - 1 or row == 0):
            k = k*(-1)
        row += k

    messageInd = 0
    for i in range(key):
        for j in range(len(message)):
            if(arr[i][j] == "*"):
                arr[i][j] = message[messageInd]
                messageInd += 1
    row =0
    col =0
    k =-1
    for i in range(len(message)):
        print(arr[row][col], end="")
        col+=1
        if(row == key -1 or row == 0):
            k = k*(-1)
        row+=k                    


    # print(arr[0])


          




    


encryption("ABCDEFGHIJ", 3)
decryption("AEIBDFHJCG" ,3)


