a=[2,4,15,25]
sorted=True
for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        sorted=False
        break
if sorted:
    print("sorted")
else:
    print("not sorted")
        

       
