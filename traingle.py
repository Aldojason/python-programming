row=int(input("enter the rows:"))
for i in range(1,row+1):
    space=" " * (row-i)
    star="*" * (2*i-1)
    print(space + star)