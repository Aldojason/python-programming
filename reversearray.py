a=[10,20,30,50]
first=0
second=len(a)-1
while first<second:
    a[first],a[second]=a[second],a[first]
    first+=1
    second-=1
print(a)