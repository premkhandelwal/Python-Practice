arr = [[0 for _ in range(16)] for _ in range(4)]

for i in range(4):
    for j in range(16):
        arr[i][j] = j+(i*16)+1

# print(arr)        

for i in arr:
    i.remove(i[7])
    i.remove(i[-1])

print(arr)    