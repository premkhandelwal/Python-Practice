"""
G e e 
"""

import math


msg = "Geeks for Geeks"
key = "HACK"  
def encryptMessage(msg):
    cipher = ""
    k_indx = 0
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key)) 

    col = len(key)
    row = int(math.ceil(msg_len / col))

    fill_null = int((row*col) - msg_len)
    msg_lst.extend('_'*fill_null)
    matrix = [["_" for _ in range(col)]  for _ in range(row)]
    messageInd = 0
    print(msg_lst)
   
    for i in range(row):
        for j in range(col):         
            if(messageInd != msg_len):
                matrix[i][j] = msg_lst[messageInd]
            else:
                break
            messageInd +=1

    for _ in range(col):
        currInd = key.index(key_lst[k_indx])
        cipher += ''.join([row1[currInd] for row1 in matrix])
        k_indx += 1  
    return cipher


"""
HACK
keyList[0] ===> A
key.index("A") ==> 1
"""
def decryptMessage(cipher):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = len(cipher)
    msg_lst = list(cipher)                                 
    col = len(key)
    row = int(math.ceil(msg_len / col)) 
    keyList = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    # print(dec_cipher)
    for _ in range(col):
        currInd = key.index(keyList[k_indx])
        for j in range(row):
            dec_cipher[j][currInd] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1    
    msg = ''.join(sum(dec_cipher, []))
    nullCount = msg.count("_")
    if(nullCount > 0):
        return msg[: -nullCount]        
    return msg

cipher = encryptMessage(msg)
print(cipher)
cipher1 = decryptMessage(cipher)
print(cipher1)