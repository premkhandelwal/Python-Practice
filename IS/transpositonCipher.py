""" 
        0 1 2 3
    0   H e l l 
    1   o   W o
    2   r l d
"""

def calculateLenNum(num):
    return len(str(num))

def encrypt(message, key):
    print(message)
    keyLen = len(str(key))
    # rowCount = len(message) % 
    rowCount = 4
    transmatrix = [["" for _ in range(keyLen)]  for _ in range(rowCount)]
    print(keyLen)
    print(rowCount)

    messageInd = 0 
    print(len(message))
    for i in range(rowCount):
        for j in range(keyLen):
            
            if(messageInd != len(message)):
                transmatrix[i][j] = message[messageInd]
            else:
                break
            messageInd +=1

    """ print(transmatrix[0][0])        
    print(transmatrix[0][1])        
    print(transmatrix[0][2])        
    print(transmatrix[0][3])   

    print(transmatrix[1][0])        
    print(transmatrix[1][1])        
    print(transmatrix[1][2])        
    print(transmatrix[1][3])        
    
    print(transmatrix[2][0])        
    print(transmatrix[2][1])        
    print(transmatrix[2][2])        
    print(transmatrix[2][3])  """  

    resArr = []     

    for i in range(keyLen):
        resString = ""
        for j in range(rowCount):
            resString += transmatrix[j][i];
        resArr.insert(i, resString)
    print(resArr)

    strKey = str(key)

    for j in range(keyLen):
        ind = int(strKey[j]) -1
        print(resArr[ind], end= "")       


encrypt("Hello World", 2134)