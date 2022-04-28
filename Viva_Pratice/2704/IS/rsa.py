from decimal import Decimal


def gcd(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
#input variables
d=0
p = 11
q = 17
message = 3
#calculate n
n = p*q
#calculate totient
totient = (p-1)*(q-1)

#calculate K
for k in range(2,totient):
    print(totient)
    if gcd(k,totient)== 1:
        break

for i in range(1,10):
    x = 1 + i*totient
    if x % k == 0:
        d = int(x/k)
        break
# local_cipher = Decimal(0)
local_cipher = pow(message,k)
cipher_text = local_cipher % n

# decrypt_t = Decimal(0)
decrypt_t= pow(cipher_text,d)
decrpyted_text = decrypt_t % n

print('Encrypted text = '+str(cipher_text))
print('Decrypted text = '+str(decrpyted_text))
