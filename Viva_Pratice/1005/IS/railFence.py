def encrypt(message, key):
    arr = [["" for _ in range(len(message))] for _ in range(key)]
    row = 0
    col = 0
    k =-1
    for i in range(len(message)):
        arr[row][col] = message[i]
        col += 1
        if(row == key -1 or row == 0):
            k = k*(-1)
        row += k  

    for i in range(key):
        for j in range(len(message)):
            if(arr[i][j] != ""):
                print(arr[i][j], end="")         
def decrypt(message, key):
    arr = [["" for _ in range(len(message))] for _ in range(key)]
    row = 0
    col = 0
    k = -1
    for i in range(len(message)):
        arr[row][col] = "*"
        col += 1
        if(row == key -1 or row == 0):
            k = k*(-1)
        row += k
    messageInd = 0
    for i in range(key):
        for j in range(len(message)):
            if(arr[i][j] == "*"):
                arr[i][j] = message[messageInd]
                messageInd += 1
    row = 0
    col = 0
    k = -1
    for i in range(len(message)):
        print(arr[row][col], end="")
        col += 1
        if(row == key -1 or row == 0):
            k = k*(-1)
        row += k                      
encrypt("ABCDEFGHIJ", 3)
print("\n")
decrypt("AEIBDFHJCG", 3)