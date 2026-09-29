n=int(input("enter n:"))
a=[]
for i in range (0,n):
    units=int(input("enter unit:"))
    a.append(units)
max=0
for j in a:
    if j>max:
        max=j
print(max)

    
