import math
msg = "Hello World"
key= "HACK"

def encrypt(msg):
    cipher = ""
    kInd = 0
    msg_len = float(len(msg))
    msg_list = list(msg)
    key_list = sorted(list(list(key)))

    colCount = len(key)
    rowCount = int(math.ceil(msg_len / colCount))

    fill_null = int((rowCount * colCount) - msg_len)
    msg_list.extend("_" * fill_null)
    matrix = [["_" for _ in range(colCount)] for _ in range(rowCount)]
    messageInd = 0

    for i in range(rowCount):
        for j in range(colCount):
            if(messageInd != msg_len):
                matrix[i][j] = msg_list[messageInd]
            else:
                break
            messageInd += 1
    print(matrix)            

    for _ in range(colCount):
        currInd = key.index(key_list[kInd])
        cipher += ''.join([row1[currInd] for row1 in matrix])
        kInd += 1
    print(cipher) 

def decrypt(cipher):
    kInd =0
    mInd = 0
    mLen = len(cipher)
    mList = list(cipher)
    colCount = len(key)
    rowCount = int(math.ceil(mLen / colCount))
    kList = sorted(list(key))
    decCipher = []
    for _  in range(rowCount):
        decCipher += [[None] * colCount]
    for _ in range(colCount):
        currInd = key.index(kList[kInd])
        for j in range(rowCount):
            decCipher[j][currInd] = mList[mInd]
            mInd+=1
        kInd += 1
    msg = ''.join(sum(decCipher, []))
    print(msg)
    nullCount = msg.count("_")
    if(nullCount >0):
        print("Message", msg[: -nullCount])
        return msg[: -nullCount]
    print("Message", msg)

encrypt(msg)
decrypt("e llWdHorlo_")