a = 6
b = 1
c = 1
s = "aabaacaa"


#  % 2
maxi = max(a,b)
maxi = max(maxi, c)
dict1 = {"a": a, "b": b, "c":c}
keys =list(dict1.keys())
values =list(dict1.values())

position = values.index(max(values))
maxEle = keys[position]
# print(dict1.keys(max(dict1.values)))
ansString = ""
leng = a + b+ c
while(leng > 0):
    if(a % 2 == 1):
        ansString += "a"*(a)
        a = a - 1
    elif(a != 0):
        a = a - 2
        ansString += "a"*2

    if(b % 2 == 1):
        print(True)
        ansString += "b"*(b)
        b = b - 1
    elif(b != 0):
        ansString += "b"*(b)
        b = b - 2    
    if(c% 2 == 1):
        ansString += "c"*(c)
        c = c - 1
    elif(c != 0):
        ansString += "c"*(c)
        c = c - 2
    leng = a + b+ c               
print(ansString)


https://us-central1-qwiklabs-gcp-04-45f1d77ead2d.cloudfunctions.net/restaurant_locator