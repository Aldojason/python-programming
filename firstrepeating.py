a=[2,3,2,3,4,5,4]
f={}
for i in a:
    f[i]=f.get(i,0)+1
for i in a:
        if f[i]==1:
              print(i)
              break
