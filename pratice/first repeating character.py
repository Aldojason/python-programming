s=input("enter string:")
f={}
for i in s:
    f[i]=f.get(i,0)+1
    if f[i]>1:
        print(i)
        break
else:
    print(-1)
