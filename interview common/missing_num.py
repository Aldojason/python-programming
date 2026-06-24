lst=[1,2,3,5,7]
s=set(lst)
a=[]
ran=int(input("enter the range:"))
for i in range(1,ran+1):
    if i not in s:
        a.append(i)
print("missing numbers are:",a)
