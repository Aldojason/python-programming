a=7
b=5
c=7
maxnum=max(a,b,c)
if(a==b==c):
    print("all the numbers are equal")
else:
    if(a==maxnum):
        print("a",end=" ")
    if(b==maxnum):
        print("b",end=" ")
    if(c==maxnum):
        print("c",end=" ")