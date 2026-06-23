lst=[1,2,3,4,5,6,7]
k=int(input("enter num:"))
a=[]
for i in range(0,len(lst),k):
    a.append(lst[i:i+k])
print(a)