p = 17
q = 11
n = p * q
tot = (p-1)*(q-1)
d = 0
message = 3


def gcd(a, b):
    while(b != 0):
        c = a % b
        a = b
        b = c
    return a


print(gcd(8, 16))

for k in range(2, tot):
    if(gcd(k, tot) == 1):
        break
print(k)

for i in range(1, 10):
    x = tot*i + 1
    if(x % k == 0):
        d = int(x/k)
        break
print(x)    
print(d)

cipher = pow(message, k) % n
print(pow(cipher, d) % n)
