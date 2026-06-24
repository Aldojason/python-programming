a=[1,2,3,1,4,3,2]
f={}
for i in a:
    f[i]=f.get(i,0)+1
for k,j in f.items():
   if j==1:
       print(k)
       