"""
n = 33
tot = 20



"""

from email import message


p = 11
q = 17
n = p * q
tot = (p-1)*(q-1)
d = 0
message = 3
def gcd(a,b):
    while(b != 0):
        c = a % b 
        a = b
        b = c
    return a    

for k in range(2, tot):
    if(gcd(k, tot) == 1):
        break

for i in range(1,10):
    x = 1 + i* tot
    if(x % k == 0):
        d = int(x/k)
        break

local_cipher = pow(message,k)
decrypt_t = pow(local_cipher, d)
print(local_cipher)    
print(decrypt_t %n)