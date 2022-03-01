from math import asin, sqrt


r1 = int(input())
r2 = int(input())
a= 0
r2 = 6
d = 23
t = 0
v1 = 5
a = sqrt(pow(r1,2) - pow(d - r2, 2))
print(a)
theta = 2*asin(a/r1)
s = r1 * theta  #arc length
t = s/v1
print(t)