a=32
b=128
c=min(a,b)
for i in range(1,c+1):
    if (a%i==0 and b%i==0):
        gcd=i
print(gcd)