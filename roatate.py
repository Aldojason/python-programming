lst=list(map(int,input("enter numbers seprated by spaces:").split()))
k=int(input("enter the number of rotations:"))
for i in range(k):
    lst.insert(0,lst[-1])
    lst.pop()
print(lst)