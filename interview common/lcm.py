# lcm=a*b/hcf
a=12
b=18
for i in range(1,max(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
lcm=a*b/gcd
print(int(lcm))
